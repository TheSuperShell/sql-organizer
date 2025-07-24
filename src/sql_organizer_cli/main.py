from pathlib import Path
from typing import Annotated

import rich
import typer
from pydantic import ValidationError

from sql_organizer_file_sorter.sorter import SORTERS, sort_paths
from sql_organizer_search_engine.search import FileExtension, get_all_sql_files

app = typer.Typer()


@app.command()
def search(
    path: Annotated[
        Path, typer.Argument(help="path, where the SQL files are located")
    ] = Path("."),
    extension: Annotated[list[str], typer.Option("--extension", "-e")] = ["sql"],
    sorters: Annotated[
        list[str],
        typer.Option(
            "--sorter", "-so", help=f"Available sorters: {', '.join(SORTERS)}"
        ),
    ] = [
        "folder",
        "first_number",
    ],
) -> None:
    for sorter in sorters:
        if sorter not in SORTERS:
            rich.print(
                f"[bold red]Value Error![/bold red] sorter [bold blue]{sorter}\
[/bold blue] is invalid"
            )
            return
    try:
        extensions = [FileExtension(extension=e) for e in extension]
    except ValidationError:
        rich.print(
            "[bold red]Value Error![/bold red] Extension should not be an empty string"
        )
        return
    files = get_all_sql_files(path, extensions)
    if len(files) == 0:
        rich.print(
            f"[yellow]No files with [bold blue]\
{', '.join(e.extension for e in extensions)}\
[/bold blue] extension{'s' if len(extensions) > 1 else ''} found![/yellow]"
        )
        return
    sorted_files = sort_paths(files, [SORTERS[s] for s in sorters])

    for file in sorted_files:
        rich.print(file.absolute())
