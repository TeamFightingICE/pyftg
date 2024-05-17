from dataclasses import dataclass

from google.protobuf.message import Message

from pyftg.models.base_model import BaseModel


@dataclass
class HitArea(BaseModel):
    """
    HitArea (BaseModel): Hit area data class.
    """

    left: int = 0
    """
    left (int): The most left x coordinate of the hit box.
    """
    right: int = 0
    """
    right (int): The most right x coordinate of the hit box.
    """
    top: int = 0
    """
    top (int): The most top y coordinate of the hit box.
    """
    bottom: int = 0
    """
    bottom (int): The most bottom y coordinate of the hit box.
    """
    
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
