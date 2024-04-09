from base64 import b64decode, b64encode
from dataclasses import dataclass

from typing_extensions import List

from pyftg.models.base_model import BaseModel
from pyftg.models.fft_data import FFTData


@dataclass
class AudioData(BaseModel):
    raw_data_bytestring: str
    fft_data: List[FFTData]
    spectrogram_data_bytestring: str
    
    @property
    def raw_data_as_bytes(self):
        return b64decode(self.raw_data_bytestring)
    
    @property
    def spectrogram_data_as_bytes(self):
        return b64decode(self.spectrogram_data_bytestring)

    def to_dict(self):
        return {
            "raw_data_bytestring": self.raw_data_bytestring,
            "fft_data": [data.to_dict() for data in self.fft_data],
            "spectrogram_data_bytestring": self.spectrogram_data_bytestring
        }

    @classmethod
    def from_dict(cls, data_obj: dict):
        return AudioData(
            raw_data_bytestring=data_obj["raw_data_bytestring"],
            fft_data=[FFTData.from_dict(data) for data in data_obj["fft_data"]],
            spectrogram_data_bytestring=data_obj["spectrogram_data_bytestring"]
        )
    
    @classmethod
    def from_proto(cls, proto_obj: object):
        return AudioData(
            raw_data_bytestring=b64encode(proto_obj.raw_data_as_bytes).decode('utf-8'),
            fft_data=list(map(FFTData.from_proto, proto_obj.fft_data)),
            spectrogram_data_bytestring=b64encode(proto_obj.spectrogram_data_as_bytes).decode('utf-8')
        )

    @classmethod
    def get_default_instance(cls):
        return AudioData(raw_data_bytestring='', fft_data=[FFTData.get_default_instance() for _ in range(2)], spectrogram_data_bytestring='')
    