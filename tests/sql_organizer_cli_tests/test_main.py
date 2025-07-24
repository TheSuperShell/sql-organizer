from collections.abc import Sequence
from pathlib import Path

import pytest
from typer.testing import CliRunner

from sql_organizer_cli.main import app


@pytest.fixture(scope="module")
def cli_runner() -> CliRunner:
    return CliRunner()


def _create_files(tmp_path: Path, files: Sequence[str]):
    for file in files:
        (tmp_path / file).mkdir(parents=True, exist_ok=True)


def test_search(cli_runner, tmp_path):
    files = ["test.sql", "folder/other.txt", "bad.py"]
    _create_files(tmp_path, files)
    result = cli_runner.invoke(
        app, ["search", str(tmp_path.absolute()), "-e", "txt", "-e", "sql"]
    )
    output = result.output.replace("\n", "")
    assert result.exit_code == 0
    assert "test.sql" in output
    assert "other.txt" in output
    assert "bad.py" not in output
