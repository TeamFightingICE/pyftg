from dataclasses import dataclass, field
from typing import List

from google.protobuf.message import Message

from pyftg.models.base_model import BaseModel
from pyftg.models.fft_data import FFTData


@dataclass
class AudioData(BaseModel):
    """
    AudioData (BaseModel): Audio data class.
    """

    raw_data_bytes: bytes = b''
    """
    raw_data_bytes (bytes): Raw audio data in wave format with 2 channels and 1024 samples (800 actual samples and padded with zeros).
    """
    fft_data: List[FFTData] = field(default_factory=lambda: [FFTData(), FFTData()])
    """
    fft_data (List[FFTData]): FFT data for two channels.
    """
    spectrogram_data_bytes: bytes = b''
    """
    spectrogram_data_bytes (bytes): Spectrogram data bytes.
    """

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
