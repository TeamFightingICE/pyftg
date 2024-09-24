import logging
import time
from pathlib import Path
from threading import Thread

from pyftg.aiinterface.ai_interface import AIInterface
from pyftg.aiinterface.command_center import CommandCenter
from pyftg.models.audio_data import AudioData
from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.key import Key
from pyftg.models.round_result import RoundResult
from pyftg.models.screen_data import ScreenData

logger = logging.getLogger(__name__)
output_path = Path(__name__)


class OneSecondAI(AIInterface):
    def __init__(self):
        self.blind_flag = True
        self.current_frame_number = -1
        self.process_thread: Thread = None
        self.is_processing = False

    def name(self) -> str:
        return self.__class__.__name__

    def is_blind(self) -> bool:
        return self.blind_flag

    def initialize(self, game_data: GameData, player: bool):
        logger.info("initialize")
        self.input_key = Key()
        self.cc = CommandCenter()
        self.player = player

    def get_non_delay_frame_data(self, frame_data: FrameData):
        pass
        
    def input(self):
        return self.input_key
        
    def get_information(self, frame_data: FrameData, is_control: bool):
        self.current_frame_number = frame_data.current_frame_number
        self.cc.set_frame_data(frame_data, self.player)
    
    def get_screen_data(self, screen_data: ScreenData):
        pass
    
    def get_audio_data(self, audio_data: AudioData):
        pass
        
    def processing(self):
        if self.cc.get_skill_flag():
            self.input_key = self.cc.get_skill_key()
            return

        self.input_key.empty()
        self.cc.skill_cancel()

        if self.current_frame_number % 60 == 0 and not self.is_processing:
            self.is_processing = True
            self.process_thread = Thread(target=self.processing_thread)
            self.process_thread.daemon = True
            self.process_thread.start()

    def processing_thread(self):
        logger.info(f"processing start at frame: {self.current_frame_number}")
        time.sleep(0.9)  # simulate processing
        self.cc.command_call("B")
        self.is_processing = False
        logger.info(f"processing end at frame: {self.current_frame_number}")

    def round_end(self, round_result: RoundResult):
        logger.info(f"round end: {round_result}")
    
    def game_end(self):
        logger.info("game end")

    def close(self):
        pass