import pytest
from script import write_file

@pytest.fixture

def sample_file(tmp_path):
    file_path = tmp_path / "test_file.txt"
    with open(file_path, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3\n")
    return file_path

def test_write_file(tmp_path):
    lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
    file_path = tmp_path / "test_write.txt"
    write_file(file_path, lines)

    with open(file_path, 'r') as f:
        written_lines = f.readlines()
    assert written_lines == lines

