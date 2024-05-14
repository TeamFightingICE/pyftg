import asyncio
import logging

from google.protobuf.message import Message

from pyftg.aiinterface.ai_interface import AIInterface
from pyftg.aiinterface.soundgenai_interface import SoundGenAIInterface
from pyftg.interfaces.async_gateway import IAsyncGateway
from pyftg.models.enums.status_code import StatusCode
from pyftg.protoc import service_pb2
from pyftg.socket.asyncio.ai_controller import AIController
from pyftg.socket.asyncio.sound_controller import SoundController
from pyftg.socket.utils.asyncio import recv_data, send_data
from pyftg.utils.resource_loader import load_ai

logger = logging.getLogger(__name__)


class Gateway(IAsyncGateway):
    def __init__(self, host='127.0.0.1', port=50051):
        self.host = host
        self.port = port
        self.registered_agents: dict[str, AIInterface] = dict()
        self.agents: list[AIInterface] = [None, None]
        self.ais: list[AIController] = [None, None]
        self.sound_agent: SoundGenAIInterface = None
        self.sound: SoundController = None
    
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

    async def run_game(self, characters: list[str], agents: list[str], game_number: int):
        for i in range(2):
            if agents[i] == 'Sandbox':
                agents[i] = None
            elif agents[i] in self.registered_agents:
                self.agents[i] = self.registered_agents[agents[i]]

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

    async def start_ai(self):
        tasks = list()
        loop = asyncio.get_event_loop()
        for i, agent in enumerate(self.agents):
            if agent:
                self.ais[i] = AIController(self.host, self.port, agent, i == 0)
                tasks.append(loop.create_task(self.ais[i].run()))
                logger.info(f"AI controller for P{i+1} ({agent.name()}) is ready.")
        await asyncio.gather(*tasks)

    async def start_sound(self):
        tasks = list()
        loop = asyncio.get_event_loop()
        if self.sound_agent:
            self.sound = SoundController(self.host, self.port, self.sound_agent)
            tasks.append(loop.create_task(self.sound.run()))
            logger.info(f"Sound controller is ready.")
        await asyncio.gather(*tasks)

    async def close(self):
        for ai in self.ais:
            if ai:
                await ai.close()
        if self.sound:
            await self.sound.close()
