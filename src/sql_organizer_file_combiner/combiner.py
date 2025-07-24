from collections.abc import Sequence
from pathlib import Path

from sql_organizer_file.file import SqlFile


def combine_files(new_file_path: Path, files: Sequence[SqlFile]):
    with new_file_path.open("w") as f:
        f.write("\n".join(f.sql_text for f in files))
