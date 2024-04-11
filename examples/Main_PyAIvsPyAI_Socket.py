import typer
from typing_extensions import Annotated, Optional

from DisplayInfo import DisplayInfo
from KickAI import KickAI
from pyftg.socket.threading.gateway import Gateway
from pyftg.utils.logging import DEBUG, set_logging

app = typer.Typer(pretty_exceptions_enable=False)


def start_process(character: str = "ZEN", game_num: int = 1, port: int = 11111):
    gateway = Gateway(port=port)
    agent1 = KickAI()
    agent2 = DisplayInfo()
    gateway.register_ai("KickAI", agent1)
    gateway.register_ai("DisplayInfo", agent2)
    gateway.run_game([character, character], ["KickAI", "DisplayInfo"], game_num)
    gateway.close()


@app.command()
def main(
        port: Annotated[Optional[int], typer.Option(help="Port used by DareFightingICE")] = 11111):
    start_process(port=port)


if __name__ == '__main__':
    set_logging(log_level=DEBUG)
    app()
