from pathlib import Path
from typing import Annotated

import rich
import rich.errors
import typer
from pydantic import ValidationError

from sql_organizer_search_engine.search import FileExtension, get_all_sql_files

app = typer.Typer()


@app.command()
def echo(message: Annotated[str, typer.Argument(help="Message to echo")]) -> None:
    rich.print(message)
    print("done")


@app.command()
def search(
    path: Annotated[Path, typer.Argument(help="search path")] = Path("."),
    extension: Annotated[list[str], typer.Option("--extension", "-e")] = ["sql"],
) -> None:
    try:
        extensions = [FileExtension(extension=e) for e in extension]
    except ValidationError:
        rich.print(
            "[bold red]Value Error![/bold red] Extension should not be an empty string"
        )
        return
    files = get_all_sql_files(path, extensions)
    for file in files:
        rich.print(file.absolute())
