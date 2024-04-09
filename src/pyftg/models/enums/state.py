from enum import Enum

from pyftg.models.enums.int_state import IntState


class State(str, Enum):
    STAND = "stand"
    CROUCH = "crouch"
    AIR = "air"
    DOWN = "down"

    def to_int(self) -> int:
        return IntState[self.name].value
    
    @classmethod
    def from_int(cls, state: int):
        return State[IntState(state).name]
