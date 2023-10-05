from abc import ABC, abstractmethod
from .struct import GameData, FrameData, ScreenData, AudioData, RoundResult

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
