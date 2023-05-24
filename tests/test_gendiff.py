import pytest

from gendiff import generate_diff
from tests import FIXTURES_DIR


def expected_str():
    with open(f'{FIXTURES_DIR}flat_output.txt') as f:
        expected_str = f.read()
    return expected_str


def _get_file_path(file_name: str) -> str:
    return f'{FIXTURES_DIR}{file_name}'


JSON1 = _get_file_path('file1.json')
JSON2 = _get_file_path('file2.json')
YAML1 = _get_file_path('file1.yml')
YAML2 = _get_file_path('file2.yml')


@pytest.mark.parametrize(
    'filepath1, filepath2',
    [
        (JSON1, JSON2),
        (YAML1, YAML2)
    ],
    ids=[
        'file1.json - file2.json',
        'file1.yml - file2.yml',
    ],
)
def test_generate_diff(filepath1, filepath2):
    assert generate_diff(filepath1, filepath2) == expected_str()
