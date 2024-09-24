import asyncio
import logging
from asyncio import Task
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Optional

from google.protobuf.message import Message

from pyftg.aiinterface.ai_interface import AIInterface
from pyftg.aiinterface.soundgenai_interface import SoundGenAIInterface
from pyftg.aiinterface.stream_interface import StreamInterface
from pyftg.models.enums.status_code import StatusCode
from pyftg.protoc import service_pb2
from pyftg.socket.aio.ai_controller import AIController
from pyftg.socket.aio.sound_controller import SoundController
from pyftg.socket.aio.stream_controller import StreamController
from pyftg.socket.utils.asyncio import recv_data, send_data
from pyftg.utils.resource_loader import load_ai

logger = logging.getLogger(__name__)


class Gateway:
    def __init__(self, host='127.0.0.1', port=31415):
        self.host = host
        self.port = port
        self.initialize_event_loop()
        self.initialize_data()

    def initialize_event_loop(self):
        pool = ThreadPoolExecutor(max_workers=8)
        loop = asyncio.get_event_loop()
        loop.set_default_executor(pool)

    def initialize_data(self):
        self.registered_agents: Dict[str, AIInterface] = {}
        self.agents: List[Optional[AIInterface]] = [None, None]
        self.sound_agent: Optional[SoundGenAIInterface] = None
        self.stream_agents: List[StreamInterface] = []
    
    def load_agent(self, ai_names: list[str]):
        """
        Load AI agent.

        Args:
            ai_names (list[str]): List of AI names.
        """
        if ai_names[0] is None and ai_names[1] is None:
            raise Exception("At least one agent must be specified.")
        for i, ai_name in enumerate(ai_names):
            if ai_name:
                self.agents[i] = load_ai(ai_name)
    
    def register_ai(self, name: str, agent: AIInterface):
        """
        Register AI agent.

        Args:
            name (str): AI name.
            agent (AIInterface): AI agent.
        """
        self.registered_agents[name] = agent

    def register_sound(self, agent: SoundGenAIInterface):
        """
        Register sound generative AI.

        Args:
            agent (SoundGenAIInterface): Sound generative AI.
        """
        self.sound_agent = agent

    def register_stream(self, stream_agent: StreamInterface):
        """
        Register stream agent.

        Args:
            stream_agent (StreamInterface): Stream agent.
        """
        self.stream_agents.append(stream_agent)

    async def run_game(self, characters: list[str], agents: list[str], game_number: int):
        """
        Sends a request to run a game.

        Args:
            characters (list[str]): List of character names.
            agents (list[str]): List of AI names.
            game_number (int): Game number.
        """
        for i in range(2):
            if agents[i] == 'Sandbox':
                agents[i] = None
            elif agents[i] in self.registered_agents:
                self.agents[i] = self.registered_agents[agents[i]]
        try:
            reader, writer = await asyncio.open_connection(self.host, self.port)
            request: Message = service_pb2.RunGameRequest(character_1=characters[0], character_2=characters[1],
                                                        player_1=agents[0], player_2=agents[1], game_number=game_number)
            await send_data(writer, b'\x02', with_header=False)  # 2: Run Game
            await send_data(writer, request.SerializeToString())
            
            response_packet = await recv_data(reader)
            response: Message = service_pb2.RunGameResponse()
            response.ParseFromString(response_packet)

            if response.status_code is StatusCode.FAILED:
                logger.error(response.response_message)
                exit(1)

            ai_task = self.start_ai()
            run_game_task = recv_data(reader, n=1)
            await asyncio.gather(ai_task, run_game_task)

            writer.close()
            await writer.wait_closed()
        except ConnectionRefusedError:
            logger.error("Connection refused by server")
        except ConnectionResetError:
            logger.info("Connection closed by server")

    async def close_game(self):
        """
        Sends a request to close the game.
        """
        try:
            _, writer = await asyncio.open_connection(self.host, self.port)
            await send_data(writer, b'\x05', with_header=False)  # 5: Close Game
            writer.close()
            await writer.wait_closed()
        except ConnectionRefusedError:
            logger.error("Connection refused by server")

    async def start_ai(self):
        """
        Start AI controller.
        """
        try:
            tasks: List[Task] = []
            loop = asyncio.get_event_loop()
            for i, agent in enumerate(self.agents):
                if agent:
                    controller = AIController(self.host, self.port, agent, i == 0)
                    tasks.append(loop.create_task(controller.run()))
                    logger.info(f"Start P{i+1} AI controller task ({agent.name()})")
            await asyncio.gather(*tasks)
        except ConnectionRefusedError:
            logger.error("Connection refused by server")
        except ConnectionResetError:
            logger.info("Connection closed by server")

    async def start_sound(self, keep_alive: bool = False):
        """
        Start sound generative AI controller.
        """
        try:
            tasks: List[Task] = []
            loop = asyncio.get_event_loop()
            if self.sound_agent:
                controller = SoundController(self.host, self.port, self.sound_agent, keep_alive)
                tasks.append(loop.create_task(controller.run()))
                logger.info(f"Start Sound controller task")
            await asyncio.gather(*tasks)
        except ConnectionRefusedError:
            logger.error("Connection refused by server")
        except ConnectionResetError:
            logger.info("Connection closed by server")

    async def start_stream(self, keep_alive: bool = False):
        """
        Start stream controller.
        """
        try:
            tasks: List[Task] = []
            loop = asyncio.get_event_loop()
            for i, stream in enumerate(self.stream_agents):
                controller = StreamController(self.host, self.port, stream, keep_alive)
                tasks.append(loop.create_task(controller.run()))
                logger.info(f"Start Stream controller task #{i+1}")
            await asyncio.gather(*tasks)
        except ConnectionRefusedError:
            logger.error("Connection refused by server")
        except ConnectionResetError:
            logger.info("Connection closed by server")

    async def close(self):
        """
        Close the gateway.
        """
        pass
