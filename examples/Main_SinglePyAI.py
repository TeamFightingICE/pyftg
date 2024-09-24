import asyncio

import typer
from typing_extensions import Annotated, Optional

from pyftg.socket.aio.gateway import Gateway
from pyftg.utils.logging import DEBUG, set_logging

app = typer.Typer(pretty_exceptions_enable=False)


async def start_process(host: str, port: int, a1: str, a2: str):
    gateway = Gateway(host, port)
    gateway.load_agent([a1, a2])
    await gateway.start_ai()


@app.command()
def main(
        host: Annotated[Optional[str], typer.Option(help="Host used by DareFightingICE")] = "127.0.0.1",
        port: Annotated[Optional[int], typer.Option(help="Port used by DareFightingICE")] = 31415,
        a1: Annotated[Optional[str], typer.Option(help="The AI name to use for player 1")] = None,
        a2: Annotated[Optional[str], typer.Option(help="The AI name to use for player 2")] = None):
    asyncio.run(start_process(host, port, a1, a2))
    

if __name__ == '__main__':
    set_logging(log_level=DEBUG)
    app()
