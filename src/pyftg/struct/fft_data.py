class FftData:
    def __init__(self, fft_data):
        self.real_data_as_bytes: bytes = fft_data.real_data_as_bytes
        self.imaginary_data_as_bytes: bytes = fft_data.imaginary_data_as_bytes
