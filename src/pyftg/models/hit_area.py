from dataclasses import dataclass

from google.protobuf.message import Message

from pyftg.models.base_model import BaseModel


@dataclass
class HitArea(BaseModel):
    left: int
    right: int
    top: int
    bottom: int
    
    def to_dict(self):
        return {
            "left": self.left,
            "right": self.right,
            "top": self.top,
            "bottom": self.bottom
        }

    @classmethod
    def from_dict(cls, data_obj: dict):
        return HitArea(
            left=data_obj["left"],
            right=data_obj["right"],
            top=data_obj["top"],
            bottom=data_obj["bottom"]
        )
    
    @classmethod
    def from_proto(cls, proto_obj: Message):
        return HitArea(
            left=proto_obj.left,
            right=proto_obj.right,
            top=proto_obj.top,
            bottom=proto_obj.bottom
        )
    
    @classmethod
    def get_default_instance(cls):
        return HitArea(left=0, right=0, top=0, bottom=0)
