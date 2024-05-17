import asyncio
import logging
from asyncio import Task
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Optional

from google.protobuf.message import Message

from pyftg.aiinterface.ai_interface import AIInterface
from pyftg.aiinterface.soundgenai_interface import SoundGenAIInterface
from pyftg.aiinterface.stream_interface import StreamInterface
from pyftg.interfaces.async_gateway import IAsyncGateway
from pyftg.models.enums.status_code import StatusCode
from pyftg.protoc import service_pb2
from pyftg.socket.aio.ai_controller import AIController
from pyftg.socket.aio.sound_controller import SoundController
from pyftg.socket.aio.stream_controller import StreamController
from pyftg.socket.utils.asyncio import recv_data, send_data
from pyftg.utils.resource_loader import load_ai

logger = logging.getLogger(__name__)


class Gateway(IAsyncGateway):
    def __init__(self, host='127.0.0.1', port=31415):
        self.host = host
        self.port = port
        self.initialize_event_loop()
        self.initialize_data()

    def initialize_event_loop(self):
        pool = ThreadPoolExecutor(max_workers=8)
        self.event_loop = asyncio.get_event_loop()
        self.event_loop.set_default_executor(pool)

    def initialize_data(self):
        self.registered_agents: Dict[str, AIInterface] = {}
        self.agents: List[Optional[AIInterface]] = [None, None]
        self.sound_agent: Optional[SoundGenAIInterface] = None
        self.stream_agents: List[StreamInterface] = []

    def get_event_loop(self):
        return self.event_loop
    
    def load_agent(self, ai_names: list[str]):
        if ai_names[0] is None and ai_names[1] is None:
            raise Exception("At least one agent must be specified.")
        for i, ai_name in enumerate(ai_names):
            if ai_name:
                self.agents[i] = load_ai(ai_name)
    
    def register_ai(self, name: str, agent: AIInterface):
        self.registered_agents[name] = agent

    def register_sound(self, agent: SoundGenAIInterface):
        self.sound_agent = agent

    def register_stream(self, stream_agent: StreamInterface):
        self.stream_agents.append(stream_agent)

    async def run_game(self, characters: list[str], agents: list[str], game_number: int):
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

            writer.close()
            await writer.wait_closed()
            await self.start_ai()
        except ConnectionRefusedError:
            logger.error("Connection refused by server")
        except ConnectionResetError:
            logger.info("Connection closed by server")

    async def start_ai(self):
        try:
            tasks: List[Task] = []
            loop = self.get_event_loop()
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

    async def start_sound(self):
        try:
            tasks: List[Task] = []
            loop = self.get_event_loop()
            if self.sound_agent:
                controller = SoundController(self.host, self.port, self.sound_agent)
                tasks.append(loop.create_task(controller.run()))
                logger.info(f"Start Sound controller task")
            await asyncio.gather(*tasks)
        except ConnectionRefusedError:
            logger.error("Connection refused by server")
        except ConnectionResetError:
            logger.info("Connection closed by server")

    async def start_stream(self):
        try:
            tasks: List[Task] = []
            loop = self.get_event_loop()
            for i, stream in enumerate(self.stream_agents):
                controller = StreamController(self.host, self.port, stream)
                tasks.append(loop.create_task(controller.run()))
                logger.info(f"Start Stream controller task #{i+1}")
            await asyncio.gather(*tasks)
        except ConnectionRefusedError:
            logger.error("Connection refused by server")
        except ConnectionResetError:
            logger.info("Connection closed by server")
