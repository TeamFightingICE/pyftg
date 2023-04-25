from ..protoc import service_pb2, service_pb2_grpc
from ..aiinterface import AIInterface
from ..util import load_ai
from .ai_controller import AIController
import logging
import asyncio
import grpc

class Gateway:
    def __init__(self, host='127.0.0.1', port=50051):
        self.host = host
        self.port = port
        self.channel = grpc.aio.insecure_channel(
            target=f"{host}:{port}",
            compression=grpc.Compression.Gzip,
        )
        self.stub = service_pb2_grpc.ServiceStub(self.channel)
        self.registered_agents: 'dict[str, AIInterface]' = dict()
        self.agents: 'list[AIInterface]' = [None, None]
        self.ais: 'list[AIController]' = [None, None]
    
    def load_agent(self, ai_names: 'list[str]'):
        for i, ai_name in enumerate(ai_names):
            if ai_name:
                self.agents[i] = load_ai(ai_name)
    
    def register_ai(self, name: str, agent: AIInterface):
        self.registered_agents[name] = agent

    async def run_game(self, characters: 'list[str]', agents: 'list[str]', game_number: int):
        for i in range(2):
            if agents[i] == 'Sandbox':
                agents[i] = None
            elif agents[i] in self.registered_agents:
                self.agents[i] = self.registered_agents[agents[i]]
        await self.stub.RunGame(service_pb2.RunGameRequest(character_1=characters[0], character_2=characters[1], player_1=agents[0], player_2=agents[1], game_number=game_number))
        await self.start_ai()
    
    async def start_ai(self):
        tasks = list()
        loop = asyncio.get_event_loop()
        for i, agent in enumerate(self.agents):
            if agent:
                self.ais[i] = AIController(self.stub, agent, i == 0)
                tasks.append(loop.create_task(self.ais[i].run()))
                logging.info(f"AI controller for P{i+1} ({agent.name()}) is ready.")
        await asyncio.gather(*tasks)
    
    async def close(self):
        await self.channel.close()
