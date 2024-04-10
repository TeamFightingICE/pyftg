import logging

import orjson

from pyftg.aiinterface.ai_interface import AIInterface
from pyftg.models.frame_data import FrameData
from pyftg.socket.ai_controller import AIController
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

    def start_ai(self):
        for i, agent in enumerate(self.agents):
            if agent:
                self.ais[i] = AIController(self.host, self.port, agent, i == 0)
                self.ais[i].start()
                logger.info(f"AI controller for P{i+1} ({agent.name()}) is ready.")
        return [x.join() for x in self.ais if x]

    def close(self):
        pass
