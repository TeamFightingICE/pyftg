import logging

import grpc

from pyftg.aiinterface.ai_interface import AIInterface
from pyftg.grpc.threading.ai_controller import AIController
from pyftg.models.enums.status_code import StatusCode
from pyftg.protoc import service_pb2, service_pb2_grpc
from pyftg.utils.resource_loader import load_ai

logger = logging.getLogger(__name__)


class Gateway:
    def __init__(self, host='127.0.0.1', port=50051):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(
            target=f"{host}:{port}",
            compression=grpc.Compression.Gzip,
        )
        self.stub = service_pb2_grpc.ServiceStub(self.channel)
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

    def run_game(self, characters: list[str], agents: list[str], game_number: int):
        for i in range(2):
            if agents[i] == 'Sandbox':
                agents[i] = None
            elif agents[i] in self.registered_agents:
                self.agents[i] = self.registered_agents[agents[i]]
        response = self.stub.RunGame(service_pb2.RunGameRequest(character_1=characters[0], character_2=characters[1], 
                                                                player_1=agents[0], player_2=agents[1], game_number=game_number))
        if StatusCode(response.status_code) is StatusCode.FAILED:
            logger.error(response.response_message)
            exit(1)

        self.start_ai()
    
    def start_ai(self):
        for i, agent in enumerate(self.agents):
            if agent:
                self.ais[i] = AIController(self.stub, agent, i == 0)
                self.ais[i].start()
                logger.info(f"AI controller for P{i+1} ({agent.name()}) is ready.")
        return [x.join() for x in self.ais if x]
    
    def close(self):
        self.channel.close()
