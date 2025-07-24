from typing import Annotated

import typer

EchoMessage = Annotated[str, typer.Argument(help="The echo message")]


def echo(message: EchoMessage) -> None:
    print(message)
