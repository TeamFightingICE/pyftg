from dataclasses import dataclass, field
from typing import List

from google.protobuf.message import Message

from pyftg.models.base_model import BaseModel


@dataclass
class RoundResult(BaseModel):
    """
    RoundResult (BaseModel): Round result data class.
    """

    current_round: int = -1
    """
    current_round (int): The current round number.
    """
    remaining_hps: List[int] = field(default_factory=lambda: [0, 0])
    """
    remaining_hps (List[int]): Remaining hit points for both players. Index 0 is player 1, and index 1 is player 2.
    """
    elapsed_frame: int = -1
    """
    elapsed_frame (int): The number of elapsed frames.
    """
    
    def to_dict(self):
        return {
            "current_round": self.current_round,
            "remaining_hps": self.remaining_hps,
            "elapsed_frame": self.elapsed_frame
        }

    @classmethod
    def from_dict(cls, data_obj: dict):
        return RoundResult(
            current_round=data_obj["current_round"],
            remaining_hps=data_obj["remaining_hps"],
            elapsed_frame=data_obj["elapsed_frame"]
        )
    
    @classmethod
    def from_proto(cls, proto_obj: Message):
        return RoundResult(
            current_round=proto_obj.current_round,
            remaining_hps=list(map(int, proto_obj.remaining_hps)),
            elapsed_frame=proto_obj.elapsed_frame
        )
