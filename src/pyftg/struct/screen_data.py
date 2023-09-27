import gzip
import io

class ScreenData:
    def __init__(self, screen_data):
        compressed_display_bytes = io.BytesIO(screen_data.display_bytes)
        with gzip.GzipFile(fileobj=compressed_display_bytes, mode='rb') as file:
            self.display_bytes: bytes = file.read()
