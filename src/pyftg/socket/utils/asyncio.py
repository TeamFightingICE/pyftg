from asyncio.streams import StreamReader, StreamWriter


async def recv_data(reader: StreamReader, n: int = -1) -> bytes:
    if n == -1:
        header_data = await reader.readexactly(4)
        n = int.from_bytes(header_data, byteorder='little')
        if n == 0:
            return b''
    body_data = await reader.readexactly(n)
    return body_data


async def send_data(writer: StreamWriter, data: bytes, with_header: bool = True) -> None:
    if with_header:
        buffer_size = len(data).to_bytes(4, byteorder='little')
        writer.write(buffer_size)
        await writer.drain()
    writer.write(data)
    await writer.drain()
