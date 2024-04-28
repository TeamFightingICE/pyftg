from abc import ABC, abstractmethod

from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.round_result import RoundResult


class SoundGenAIInterface(ABC):
    @abstractmethod
    def initialize(self, game_data: GameData):
        pass

    @abstractmethod
    def init_round(self):
        pass

    @abstractmethod
    def processing_game(self, frame_data: FrameData):
        pass

    @abstractmethod
    def round_end(self, round_result: RoundResult):
        pass

    @abstractmethod
    def game_end(self):
        pass

    @abstractmethod
    def audio_sample(self) -> bytes:
        pass
