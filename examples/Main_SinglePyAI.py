import asyncio

import typer
from typing_extensions import Annotated, Optional

from pyftg.grpc.asyncio.gateway import Gateway
from pyftg.utils.logging import DEBUG, set_logging

app = typer.Typer(pretty_exceptions_enable=False)


async def start_process(a1: str, a2: str, port: int = 50051):
    gateway = Gateway(port=port)
    gateway.load_agent([a1, a2])
    await gateway.start_ai()
    await gateway.close()


@app.command()
def main(
        port: Annotated[Optional[int], typer.Option(help="Port used by DareFightingICE")] = 50051,
        a1: Annotated[Optional[str], typer.Option(help="The AI name to use for player 1")] = None,
        a2: Annotated[Optional[str], typer.Option(help="The AI name to use for player 2")] = None):
    asyncio.run(start_process(a1, a2, port=port))
    

if __name__ == '__main__':
    set_logging(log_level=DEBUG)
    app()
