import asyncio

import typer
from typing_extensions import Annotated, Optional

from KickAI import KickAI
from pyftg.socket.aio.gateway import Gateway
from pyftg.utils.logging import DEBUG, set_logging

app = typer.Typer(pretty_exceptions_enable=False)


async def start_process(host: str, port: int, character: str = "ZEN", game_num: int = 1):
    gateway = Gateway(host, port)
    agent1 = KickAI()
    gateway.register_ai("KickAI", agent1)
    await gateway.run_game([character, character], ["KickAI", "Keyboard"], game_num)


@app.command()
def main(
        host: Annotated[Optional[str], typer.Option(help="Host used by DareFightingICE")] = "127.0.0.1",
        port: Annotated[Optional[int], typer.Option(help="Port used by DareFightingICE")] = 31415):
    asyncio.run(start_process(host, port))


if __name__ == '__main__':
    set_logging(log_level=DEBUG)
    app()
