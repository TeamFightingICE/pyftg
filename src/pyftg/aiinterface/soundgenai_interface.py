from abc import ABC, abstractmethod

from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.round_result import RoundResult


class SoundGenAIInterface(ABC):
    @abstractmethod
    def initialize(self, game_data: GameData) -> None:
        pass

    @abstractmethod
    def init_round(self) -> None:
        pass

    @abstractmethod
    def processing_game(self, frame_data: FrameData) -> None:
        pass

    @abstractmethod
    def round_end(self, round_result: RoundResult) -> None:
        pass

    @abstractmethod
    def game_end(self) -> None:
        pass

    @abstractmethod
    def audio_sample(self) -> bytes:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
