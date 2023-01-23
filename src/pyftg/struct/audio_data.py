from .fft_data import FftData
from array import array
import numpy as np

class AudioData:
    def __init__(self, audio_data):
        self.raw_data_as_bytes: bytes = audio_data.raw_data_as_bytes
        self.fft_data = [FftData(x) for x in audio_data.fft_data]
        self.spectrogram_data_as_bytes: bytes = audio_data.spectrogram_data_as_bytes
    
    def transform_data(self):
        self.raw_data = np.reshape(array('f', self.raw_data_as_bytes), (2, 1024))
