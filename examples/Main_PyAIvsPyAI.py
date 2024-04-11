import asyncio

import typer
from typing_extensions import Annotated, Optional

from DisplayInfo import DisplayInfo
from KickAI import KickAI
from pyftg.utils.gateway import get_async_gateway
from pyftg.utils.logging import DEBUG, set_logging

app = typer.Typer(pretty_exceptions_enable=False)


async def start_process(host: str, port: int, use_socket: bool, character: str = "ZEN", game_num: int = 1):
    gateway = get_async_gateway(host, port, use_socket)
    agent1 = KickAI()
    agent2 = DisplayInfo()
    gateway.register_ai("KickAI", agent1)
    gateway.register_ai("DisplayInfo", agent2)
    await gateway.run_game([character, character], ["KickAI", "DisplayInfo"], game_num)
    await gateway.close()


@app.command()
def main(
        host: Annotated[Optional[str], typer.Option(help="Host used by DareFightingICE")] = "127.0.0.1",
        port: Annotated[Optional[int], typer.Option(help="Port used by DareFightingICE")] = 50051,
        use_socket: Annotated[Optional[bool], typer.Option(help="Use socket instead of gRPC")] = False):
    asyncio.run(start_process(host, port, use_socket))


if __name__ == '__main__':
    set_logging(log_level=DEBUG)
    app()
