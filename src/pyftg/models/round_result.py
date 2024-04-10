from dataclasses import dataclass
from typing import List

from google.protobuf.message import Message

from pyftg.models.base_model import BaseModel


@dataclass
class RoundResult(BaseModel):
    current_round: int
    remaining_hps: List[int]
    elapsed_frame: int
    
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
    
    @classmethod
    def get_default_instance(cls):
        return RoundResult(current_round=0, remaining_hps=[0, 0], elapsed_frame=0)
