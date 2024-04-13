from pyftg.interfaces.async_gateway import IAsyncGateway


def get_async_gateway(host: str, port: int, use_grpc: bool = False) -> IAsyncGateway:
    if use_grpc:
        from pyftg.grpc.asyncio.gateway import Gateway as GrpcGateway
        return GrpcGateway(host, port)
    else:
        from pyftg.socket.asyncio.gateway import Gateway as SocketGateway
        return SocketGateway(host, port)
