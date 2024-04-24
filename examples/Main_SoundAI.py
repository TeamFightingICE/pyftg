import asyncio

import typer
from typing_extensions import Annotated, Optional

from pyftg.socket.asyncio.generative_sound_gateway import \
    GenerativeSoundGateway
from pyftg.utils.logging import DEBUG, set_logging
from TestSoundAI import TestSoundAI

app = typer.Typer(pretty_exceptions_enable=False)


async def start_process(host: str, port: int):
    gateway = GenerativeSoundGateway(host, port)
    sound_ai = TestSoundAI()
    gateway.set_sound_ai(sound_ai)
    await gateway.run()
    await gateway.close()


@app.command()
def main(
        host: Annotated[Optional[str], typer.Option(help="Host used by DareFightingICE")] = "127.0.0.1",
        port: Annotated[Optional[int], typer.Option(help="Port used by DareFightingICE")] = 12345):
    asyncio.run(start_process(host, port))


if __name__ == '__main__':
    set_logging(log_level=DEBUG)
    app()
