from ..struct import AudioData, ScreenData, FrameData, GameData, RoundResult, Key

class AIInterface:
    def name(self) -> str:
        pass

    def is_blind(self) -> bool:
        pass

    def initialize(self, game_data: GameData, player_number: bool):
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
