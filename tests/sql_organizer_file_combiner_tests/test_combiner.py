from sql_organizer_file.file import SqlFile
from sql_organizer_file_combiner.combiner import combine_files


def test_combiner(tmp_path):
    results = tmp_path / "results.sql"
    combine_files(
        results,
        [
            SqlFile(file_name="example 1", sql_text="SELECT 1;"),
            SqlFile(file_name="example 2", sql_text="SELECT 2;"),
        ],
    )
    assert results.exists()
    with results.open() as f:
        text = f.read()
    assert text == "SELECT 1;\nSELECT 2;"
