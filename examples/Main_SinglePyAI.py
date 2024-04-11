import asyncio

import typer
from typing_extensions import Annotated, Optional

from pyftg.utils.gateway import get_async_gateway
from pyftg.utils.logging import DEBUG, set_logging

app = typer.Typer(pretty_exceptions_enable=False)


async def start_process(host: str, port: int, use_socket: bool, a1: str, a2: str):
    gateway = get_async_gateway(host, port, use_socket)
    gateway.load_agent([a1, a2])
    await gateway.start_ai()
    await gateway.close()


@app.command()
def main(
        host: Annotated[Optional[str], typer.Option(help="Host used by DareFightingICE")] = "127.0.0.1",
        port: Annotated[Optional[int], typer.Option(help="Port used by DareFightingICE")] = 50051,
        use_socket: Annotated[Optional[bool], typer.Option(help="Use socket instead of gRPC")] = False,
        a1: Annotated[Optional[str], typer.Option(help="The AI name to use for player 1")] = None,
        a2: Annotated[Optional[str], typer.Option(help="The AI name to use for player 2")] = None):
    asyncio.run(start_process(host, port, use_socket, a1, a2))
    

if __name__ == '__main__':
    set_logging(log_level=DEBUG)
    app()
