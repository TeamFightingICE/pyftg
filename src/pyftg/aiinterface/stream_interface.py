from abc import ABC

from pyftg.models.audio_data import AudioData
from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.round_result import RoundResult
from pyftg.models.screen_data import ScreenData


class StreamInterface(ABC):
    def get_frame_data_flag(self) -> bool:
        return False

    def get_audio_data_flag(self) -> bool:
        return False

    def get_screen_data_flag(self) -> bool:
        return False
    
    def initialize(self, game_data: GameData) -> None:
        pass

    def get_information(self, frame_data: FrameData) -> None:
        pass

    def get_audio_data(self, audio_data: AudioData) -> None:
        pass

    def get_screen_data(self, screen_data: ScreenData) -> None:
        pass

    def processing(self) -> None:
        pass

    def round_end(self, round_result: RoundResult) -> None:
        pass

    def game_end(self) -> None:
        pass

    def close(self) -> None:
        pass
