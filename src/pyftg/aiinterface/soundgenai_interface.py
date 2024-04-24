from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.round_result import RoundResult


class SoundGenAIInterface:
    def initialize(self, game_data: GameData):
        pass

    def processing_game(self, frame_data: FrameData):
        pass

    def round_end(self, round_result: RoundResult):
        pass

    def game_end(self):
        pass

    def audio_sample(self) -> bytes:
        pass
