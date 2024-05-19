from abc import ABC, abstractmethod

from pyftg.aiinterface.ai_interface import AIInterface
from pyftg.aiinterface.soundgenai_interface import SoundGenAIInterface


class IAsyncGateway(ABC):
    """
    Abstract class for asynchronous gateway.
    """

    @abstractmethod
    def load_agent(self, ai_names: list[str]):
        """
        Load AI agent.

        Args:
            ai_names (list[str]): List of AI names.
        """
        pass

    @abstractmethod
    def register_ai(self, name: str, agent: AIInterface):
        """
        Register AI agent.

        Args:
            name (str): AI name.
            agent (AIInterface): AI agent.
        """
        pass

    @abstractmethod
    def register_sound(self, agent: SoundGenAIInterface):
        """
        Register sound generative AI.

        Args:
            agent (SoundGenAIInterface): Sound generative AI.
        """
        pass

    @abstractmethod
    async def run_game(self, characters: list[str], agents: list[str], game_number: int):
        """
        Sends a request to run a game.

        Args:
            characters (list[str]): List of character names.
            agents (list[str]): List of AI names.
            game_number (int): Game number.
        """
        pass

    @abstractmethod
    async def start_ai(self):
        """
        Start AI controller.
        """
        pass

    @abstractmethod
    async def start_sound(self):
        """
        Start sound generative AI controller.
        """
        pass

    @abstractmethod
    async def close(self):
        """
        Close the gateway.
        """
        pass
