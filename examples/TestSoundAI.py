import logging

from pyftg.aiinterface.soundgenai_interface import SoundGenAIInterface
from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.round_result import RoundResult

logger = logging.getLogger(__name__)


class TestSoundAI(SoundGenAIInterface):
    def __init__(self):
        self.audio_sample_bytes = bytes(8192)

    def initialize(self, game_data: GameData):
        logger.info("initialize")

    def init_round(self):
        logger.info("init round")

    def processing_game(self, frame_data: FrameData):
        frame_number = frame_data.current_frame_number
        logger.info(f"processing game: {frame_number}")

    def round_end(self, round_result: RoundResult):
        logger.info("round end")

    def game_end(self):
        logger.info("game end")

    def audio_sample(self) -> bytes:
        return self.audio_sample_bytes
    
    def close(self):
        logger.info("close")
