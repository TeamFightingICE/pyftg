from dataclasses import dataclass

from google.protobuf.message import Message

from pyftg.models.base_model import BaseModel


@dataclass
class FFTData(BaseModel):
    """
    FFTData (BaseModel): FFT data class.
    """

    real_data_bytes: bytes = b''
    """
    real_data_bytes (bytes): Real part of the FFT data.
    """
    imaginary_data_bytes: bytes = b''
    """
    imaginary_data_bytes (bytes): Imaginary part of the FFT data.
    """
    
    def to_dict(self):
        return {
            "real_data_bytes": self.real_data_bytes,
            "imaginary_data_bytes": self.imaginary_data_bytes
        }

    @classmethod
    def from_dict(cls, data_obj: dict):
        return FFTData(
            real_data_bytes=data_obj["real_data_bytes"],
            imaginary_data_bytes=data_obj["imaginary_data_bytes"]
        )
    
    @classmethod
    def from_proto(cls, proto_obj: Message):
        return FFTData(
            real_data_bytes=proto_obj.real_data_as_bytes,
            imaginary_data_bytes=proto_obj.imaginary_data_as_bytes
        )
