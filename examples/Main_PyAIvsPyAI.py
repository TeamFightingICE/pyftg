import asyncio

import typer
from typing_extensions import Annotated, Optional

from DisplayInfo import DisplayInfo
from KickAI import KickAI
from pyftg.asyncio.gateway import Gateway
from pyftg.utils.logging import DEBUG, set_logging

app = typer.Typer(pretty_exceptions_enable=False)


async def start_process(character: str = "ZEN", game_num: int = 1, port: int = 50051):
    gateway = Gateway(port=port)
    agent1 = KickAI()
    agent2 = DisplayInfo()
    gateway.register_ai("KickAI", agent1)
    gateway.register_ai("DisplayInfo", agent2)
    await gateway.run_game([character, character], ["KickAI", "MctsAi"], game_num)
    await gateway.close()


@app.command()
def main(
        port: Annotated[Optional[int], typer.Option(help="Port used by DareFightingICE")] = 50051):
    asyncio.run(start_process(port=port))


if __name__ == '__main__':
    set_logging(log_level=DEBUG)
    app()
