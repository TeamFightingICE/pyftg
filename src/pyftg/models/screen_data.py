import gzip
from dataclasses import dataclass

from google.protobuf.message import Message

from pyftg.models.base_model import BaseModel


@dataclass
class ScreenData(BaseModel):
    """
    ScreenData (BaseModel): Screen data class.
    """

    display_bytes: bytes = b''
    """
    display_bytes (bytes): Display data bytes.
    """

    def to_dict(self):
        return {
            "display_bytes": self.display_bytes
        }

    @classmethod
    def from_dict(cls, data_obj: dict):
        return ScreenData(
            display_bytes=data_obj["display_bytes"]
        )
    
    @classmethod
    def from_proto(cls, proto_obj: Message, decompress=True):
        display_bytes: bytes = proto_obj.display_bytes
        if decompress:
            display_bytes = gzip.decompress(display_bytes)
        return ScreenData(
            display_bytes=display_bytes
        )
