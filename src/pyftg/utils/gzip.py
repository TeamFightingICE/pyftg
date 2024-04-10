from contextlib import closing
from gzip import GzipFile
from io import BytesIO


def gzip_decompress(compressed_bytes: bytes) -> bytes:
    with closing(GzipFile(fileobj=BytesIO(compressed_bytes), mode='rb')) as file:
        return file.read()
