from abc import ABC, abstractmethod

from pyftg.models.audio_data import AudioData
from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.round_result import RoundResult
from pyftg.models.screen_data import ScreenData


class ObserverHandler(ABC):
    @abstractmethod
    def on_initialize(self, game: GameData):
        pass

    @abstractmethod
    def on_game_update(self, frame: FrameData, screen: ScreenData, audio: AudioData):
        pass

    @abstractmethod
    def on_round_end(self, result: RoundResult, game_end_flag: bool):
        pass
