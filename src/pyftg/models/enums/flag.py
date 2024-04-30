from enum import Enum


class Flag(int, Enum):
    EMPTY = 0
    INITIALIZE = 1
    INIT_ROUND = 2
    PROCESSING = 3
    ROUND_END = 4
    GAME_END = 5
