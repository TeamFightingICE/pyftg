from base64 import b64decode, b64encode
from contextlib import closing
from dataclasses import dataclass
from pyftg.utils.gzip import gzip_decompress

from google.protobuf.message import Message

from pyftg.models.base_model import BaseModel


@dataclass
class ScreenData(BaseModel):
    display_bytestring: str
    
    @property
    def display_as_bytes(self):
        return b64decode(self.display_bytestring)

    def to_dict(self):
        return {
            "display_bytestring": self.display_bytestring
        }

    @classmethod
    def from_dict(cls, data_obj: dict, decompress=False):
        display_bytestring: str = data_obj["display_bytestring"]
        if decompress:
            display_bytes = gzip_decompress(b64decode(data_obj["display_bytestring"]))
            display_bytestring = b64encode(display_bytes).decode('utf-8')

        return ScreenData(
            display_bytestring=display_bytestring
        )
    
    @classmethod
    def from_proto(cls, proto_obj: Message, decompress=True):
        display_bytes: bytes = proto_obj.display_bytes
        if decompress:
            display_bytes = gzip_decompress(display_bytes)

        return ScreenData(
            display_bytestring=b64encode(display_bytes).decode('utf-8')
        )
    
    @classmethod
    def get_default_instance(cls):
        return ScreenData(display_bytestring='')
