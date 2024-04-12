from socket import socket


def recv_data(client: socket, n: int = -1) -> bytes:
    if n == -1:
        header_data = client.recv(4)
        n = int.from_bytes(header_data, byteorder='little')
        if n == 0:
            return None
    body_data = client.recv(n)
    return body_data


def send_data(client: socket, data: bytes, with_header: bool = True) -> None:
    if with_header:
        buffer_size = len(data).to_bytes(4, byteorder='little')
        client.send(buffer_size)
    client.send(data)
