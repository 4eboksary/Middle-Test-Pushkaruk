import pytest
from script import read_file

@pytest.fixture

def sample_file(tmp_path):
    file_path = tmp_path / "test_file.txt"
    with open(file_path, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3\n")
    return file_path

def test_read_file(sample_file):
    lines = read_file(sample_file)
    assert len(lines) == 3
    assert "Line 1\n" in lines
    assert "Line 4\n" not in lines