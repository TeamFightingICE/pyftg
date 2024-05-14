from abc import ABC, abstractmethod

from pyftg.aiinterface.ai_interface import AIInterface
from pyftg.aiinterface.soundgenai_interface import SoundGenAIInterface


class IAsyncGateway(ABC):
    @abstractmethod
    def load_agent(self, ai_names: list[str]):
        pass

    @abstractmethod
    def register_ai(self, name: str, agent: AIInterface):
        pass

    @abstractmethod
    def register_sound(self, agent: SoundGenAIInterface):
        pass

    @abstractmethod
    async def run_game(self, characters: list[str], agents: list[str], game_number: int):
        pass

    @abstractmethod
    async def start_ai(self):
        pass

    @abstractmethod
    async def start_sound(self):
        pass

    @abstractmethod
    async def close(self):
        pass
