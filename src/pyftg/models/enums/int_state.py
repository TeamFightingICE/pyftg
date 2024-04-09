from enum import Enum


class IntState(int, Enum):
    STAND = 0
    CROUCH = 1
    AIR = 2
    DOWN = 3
