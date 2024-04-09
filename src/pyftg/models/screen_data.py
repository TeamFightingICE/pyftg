from base64 import b64decode, b64encode
from contextlib import closing
from dataclasses import dataclass
from gzip import GzipFile
from io import BytesIO

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
    def from_dict(cls, data_obj: dict):
        return ScreenData(
            display_bytestring=data_obj["display_bytestring"]
        )
    
    @classmethod
    def from_proto(cls, proto_obj: object):
        compressed_display_bytes = BytesIO(proto_obj.display_bytes)
        with closing(GzipFile(fileobj=compressed_display_bytes, mode='rb')) as file:
            display_bytes = file.read()

        return ScreenData(
            display_bytestring=b64encode(display_bytes).decode('utf-8')
        )
    
    @classmethod
    def get_default_instance(cls):
        return ScreenData(display_bytestring='')
