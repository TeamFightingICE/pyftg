import asyncio
import logging

import orjson

from pyftg.aiinterface.ai_interface import AIInterface
from pyftg.models.enums.status_code import StatusCode
from pyftg.socket.asyncio.ai_controller import AIController
from pyftg.socket.models.run_game_request import RunGameRequest
from pyftg.socket.models.run_game_response import RunGameResponse
from pyftg.utils.resource_loader import load_ai

logger = logging.getLogger(__name__)


class Gateway:
    def __init__(self, host='127.0.0.1', port=11111):
        self.host = host
        self.port = port
        self.registered_agents: dict[str, AIInterface] = dict()
        self.agents: list[AIInterface] = [None, None]
        self.ais: list[AIController] = [None, None]
    
    def load_agent(self, ai_names: list[str]):
        if ai_names[0] is None and ai_names[1] is None:
            raise Exception("At least one agent must be specified.")
        for i, ai_name in enumerate(ai_names):
            if ai_name:
                self.agents[i] = load_ai(ai_name)
    
    def register_ai(self, name: str, agent: AIInterface):
        self.registered_agents[name] = agent

    async def run_game(self, characters: list[str], agents: list[str], game_number: int):
        for i in range(2):
            if agents[i] == 'Sandbox':
                agents[i] = None
            elif agents[i] in self.registered_agents:
                self.agents[i] = self.registered_agents[agents[i]]
        reader, writer = await asyncio.open_connection(self.host, self.port)
        request = RunGameRequest(character_1=characters[0], character_2=characters[1], player_1=agents[0], player_2=agents[1], game_number=game_number)
        writer.write(b'\x02')  # RunGame
        await writer.drain()
        writer.write(request.to_json())
        await writer.drain()
        response = RunGameResponse.from_dict(orjson.loads(await reader.read(256)))
        if response.status_code is StatusCode.FAILED:
            logger.error(response.response_message)
            exit(1)
        writer.close()
        await writer.wait_closed()
        self.start_ai()

    async def start_ai(self):
        tasks = list()
        loop = asyncio.get_event_loop()
        for i, agent in enumerate(self.agents):
            if agent:
                self.ais[i] = AIController(self.host, self.port, agent, i == 0)
                tasks.append(loop.create_task(self.ais[i].run()))
                logger.info(f"AI controller for P{i+1} ({agent.name()}) is ready.")
        await asyncio.gather(*tasks)

    async def close(self):
        for ai in self.ais:
            if ai:
                ai.writer.close()
                await ai.writer.drain()
