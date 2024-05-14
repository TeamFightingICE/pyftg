from abc import ABC, abstractmethod

from pyftg.models.audio_data import AudioData
from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.round_result import RoundResult
from pyftg.models.screen_data import ScreenData


class StreamInterface(ABC):
    @abstractmethod
    def initialize(self, game_data: GameData) -> None:
        pass

    @abstractmethod
    def get_information(self, frame_data: FrameData) -> None:
        pass

    @abstractmethod
    def get_audio_data(self, audio_data: AudioData) -> None:
        pass

    @abstractmethod
    def get_screen_data(self, screen_data: ScreenData) -> None:
        pass

    @abstractmethod
    def processing(self) -> None:
        pass

    @abstractmethod
    def round_end(self, round_result: RoundResult) -> None:
        pass

    @abstractmethod
    def game_end(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
