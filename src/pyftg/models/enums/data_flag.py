from enum import Enum


class DataFlag(int, Enum):
    ALL = 0
    FRAME_DATA = 1
    SCREEN_DATA = 2
    AUDIO_DATA = 3
