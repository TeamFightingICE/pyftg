import logging

from pyftg.aiinterface.sound_ai_interface import SoundAIInterface
from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.round_result import RoundResult

logger = logging.getLogger(__name__)


class TestSoundAI(SoundAIInterface):
    def __init__(self):
        self.audio_sample_bytes = bytes(8192)

    def initialize(self, game_data: GameData):
        logger.info("initialize")

    def processing_game(self, frame_data: FrameData):
        logger.info("processing game")

    def round_end(self, round_result: RoundResult):
        logger.info("round end")

    def game_end(self):
        logger.info("game end")

    def audio_sample(self) -> bytes:
        return self.audio_sample_bytes
