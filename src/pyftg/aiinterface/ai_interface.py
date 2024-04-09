from pyftg.models.audio_data import AudioData
from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.key import Key
from pyftg.models.round_result import RoundResult
from pyftg.models.screen_data import ScreenData


class AIInterface:
    def name(self) -> str:
        pass

    def is_blind(self) -> bool:
        pass

    def initialize(self, game_data: GameData, player_number: bool):
        pass

    def get_non_delay_frame_data(self, frame_data: FrameData):
        pass

    def get_information(self, frame_data: FrameData, is_control: bool, non_delay_frame_data: FrameData):
        pass

    def get_screen_data(self, screen_data: ScreenData):
        pass

    def get_audio_data(self, audio_data: AudioData):
        pass

    def processing(self):
        pass

    def input(self) -> Key:
        pass

    def round_end(self, round_result: RoundResult):
        pass

    def game_end(self):
        pass
