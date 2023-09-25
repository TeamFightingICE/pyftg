from pyftg.struct import FrameData, ScreenData, AudioData, RoundResult
from pyftg import ObserverHandler
import logging

class Collector(ObserverHandler):
    def __init__(self) -> None:
        self.frames = list()

    def on_game_update(self, frame_data: FrameData, screen_data: ScreenData, audio_data: AudioData):
        if frame_data.current_frame_number % 60 == 0:
            logging.info('round number: %s', frame_data.current_frame_number)
            self.frames.append(frame_data)

    def on_round_end(self, round_result: RoundResult):
        logging.info('round end: %s', round_result.elapsed_frame)
        logging.info('len: %s', len(self.frames))
        self.frames.clear()

    def on_game_end(self, round_result: RoundResult):
        logging.info('game end: %s', round_result.elapsed_frame)
        logging.info('len: %s', len(self.frames))
        self.frames.clear()