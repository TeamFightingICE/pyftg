from dataclasses import dataclass
from typing import List

from google.protobuf.message import Message

from pyftg.models.base_model import BaseModel
from pyftg.models.fft_data import FFTData


@dataclass
class AudioData(BaseModel):
    raw_data_bytes: str
    fft_data: List[FFTData]
    spectrogram_data_bytes: str

    def to_dict(self):
        return {
            "raw_data_bytes": self.raw_data_bytes,
            "fft_data": [data.to_dict() for data in self.fft_data],
            "spectrogram_data_bytes": self.spectrogram_data_bytes
        }

    @classmethod
    def from_dict(cls, data_obj: dict):
        return AudioData(
            raw_data_bytes=data_obj["raw_data_bytes"],
            fft_data=[FFTData.from_dict(data) for data in data_obj["fft_data"]],
            spectrogram_data_bytes=data_obj["spectrogram_data_bytes"]
        )
    
    @classmethod
    def from_proto(cls, proto_obj: Message):
        return AudioData(
            raw_data_bytes=proto_obj.raw_data_as_bytes,
            fft_data=list(map(FFTData.from_proto, proto_obj.fft_data)),
            spectrogram_data_bytes=proto_obj.spectrogram_data_as_bytes
        )

    @classmethod
    def get_default_instance(cls):
        return AudioData(raw_data_bytes=b'', fft_data=[FFTData.get_default_instance() for _ in range(2)], spectrogram_data_bytes=b'')
    