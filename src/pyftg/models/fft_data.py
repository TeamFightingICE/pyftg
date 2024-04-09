from base64 import b64decode, b64encode
from dataclasses import dataclass

from pyftg.models.base_model import BaseModel


@dataclass
class FFTData(BaseModel):
    real_data_bytestring: str
    imaginary_data_bytestring: str

    @property
    def real_data_as_bytes(self):
        return b64decode(self.real_data_bytestring)
    
    @property
    def imaginary_data_as_bytes(self):
        return b64decode(self.imaginary_data_bytestring)
    
    def to_dict(self):
        return {
            "real_data_bytestring": self.real_data_bytestring,
            "imaginary_data_bytestring": self.imaginary_data_bytestring
        }

    @classmethod
    def from_dict(cls, data_obj: dict):
        return FFTData(
            real_data_bytestring=data_obj["real_data_bytestring"],
            imaginary_data_bytestring=data_obj["imaginary_data_bytestring"]
        )
    
    @classmethod
    def from_proto(cls, proto_obj: object):
        return FFTData(
            real_data_bytestring=b64encode(proto_obj.real_data_as_bytes).decode('utf-8'),
            imaginary_data_bytestring=b64encode(proto_obj.imaginary_data_as_bytes).decode('utf-8')
        )

    @classmethod
    def get_default_instance(cls):
        return FFTData(real_data_bytestring='', imaginary_data_bytestring='')