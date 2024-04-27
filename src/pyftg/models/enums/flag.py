from enum import Enum


class Flag(int, Enum):
    EMPTY = 0
    INITIALIZE = 1
    PROCESSING = 2
    ROUND_END = 3
    GAME_END = 4
    INIT_ROUND = 5
