from abc import ABC, abstractmethod

from pyftg.models.audio_data import AudioData
from pyftg.models.frame_data import FrameData
from pyftg.models.game_data import GameData
from pyftg.models.key import Key
from pyftg.models.round_result import RoundResult
from pyftg.models.screen_data import ScreenData


class AIInterface(ABC):
    """
    Abstract class for AI interface.
    """

    @abstractmethod
    def name(self) -> str:
        """
        Get AI name.

        Return:
            str: AI name.
        """
        pass

    @abstractmethod
    def is_blind(self) -> bool:
        """
        Get blind flag.

        Return:
            bool: Blind flag.
        """
        pass

    @abstractmethod
    def initialize(self, game_data: GameData, player_number: bool):
        """
        Initialize AI.

        Args:
            game_data (GameData): Game data.
            player_number (bool): Player number.
        """
        pass

    @abstractmethod
    def get_non_delay_frame_data(self, frame_data: FrameData):
        """
        Get non-delay frame data.

        Args:
            frame_data (FrameData): Frame data.
        """
        pass

    @abstractmethod
    def get_information(self, frame_data: FrameData, is_control: bool):
        """
        Get information.

        Args:
            frame_data (FrameData): Frame data.
            is_control (bool): Is control.
        """
        pass

    @abstractmethod
    def get_screen_data(self, screen_data: ScreenData):
        """
        Get screen data.

        Args:
            screen_data (ScreenData): Screen data.
        """
        pass

    @abstractmethod
    def get_audio_data(self, audio_data: AudioData):
        """
        Get audio data.

        Args:
            audio_data (AudioData): Audio data.
        """
        pass

    @abstractmethod
    def processing(self):
        """
        Processing.
        """
        pass

    @abstractmethod
    def input(self) -> Key:
        """
        Get AI input.

        Return:
            Key: AI input key.
        """
        pass

    @abstractmethod
    def round_end(self, round_result: RoundResult):
        """
        Round end.

        Args:
            round_result (RoundResult): Round result.
        """
        pass

    @abstractmethod
    def game_end(self):
        """
        Game end.
        """
        pass

    @abstractmethod
    def close(self):
        pass
