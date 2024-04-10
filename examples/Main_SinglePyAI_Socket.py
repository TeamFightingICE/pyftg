import typer
from typing_extensions import Annotated, Optional

from pyftg.socket.gateway import Gateway
from pyftg.utils.logging import DEBUG, set_logging

app = typer.Typer(pretty_exceptions_enable=False)


def start_process(a1: str, a2: str, port: int = 11111):
    gateway = Gateway(port=port)
    gateway.load_agent([a1, a2])
    gateway.start_ai()
    gateway.close()


@app.command()
def main(
        port: Annotated[Optional[int], typer.Option(help="Port used by DareFightingICE")] = 11111,
        a1: Annotated[Optional[str], typer.Option(help="The AI name to use for player 1")] = None,
        a2: Annotated[Optional[str], typer.Option(help="The AI name to use for player 2")] = None):
    start_process(a1, a2, port=port)
    

if __name__ == '__main__':
    set_logging(log_level=DEBUG)
    app()