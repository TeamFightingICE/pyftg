from enum import Enum


class StatusCode(int, Enum):
    SUCCESS = 0
    FAILED = 1
    UNKNOWN = 2
