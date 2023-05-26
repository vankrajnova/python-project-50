import pytest
from gendiff import generate_diff
from tests import FIXTURES_DIR


def _get_expected_output_by(file_name: str) -> str:
    print(f'file name=', file_name)
    with open(f'{FIXTURES_DIR}{file_name}') as f:
        expected_str = f.read()
    return expected_str


def _get_file_path_by(file_name: str) -> str:
    return f'{FIXTURES_DIR}{file_name}'


JSON1 = _get_file_path_by('file1.json')
JSON2 = _get_file_path_by('file2.json')
YAML1 = _get_file_path_by('file1.yml')
YAML2 = _get_file_path_by('file2.yml')
NESTED_JSON1 = _get_file_path_by('nested_file1.json')
NESTED_JSON2 = _get_file_path_by('nested_file2.json')
NESTED_YAML1 = _get_file_path_by('nested_file1.yml')
NESTED_YAML2 = _get_file_path_by('nested_file2.yml')
FLAT_OUTPUT = _get_expected_output_by('flat_output.txt')
NESTED_OUTPUT = _get_expected_output_by('nested_output.txt')


@pytest.mark.parametrize(
    'filepath1, filepath2, output',
    [
        (JSON1, JSON2, FLAT_OUTPUT),
        (YAML1, YAML2, FLAT_OUTPUT),
        (NESTED_JSON1, NESTED_JSON2, NESTED_OUTPUT),
        (NESTED_YAML1, NESTED_YAML2, NESTED_OUTPUT),
    ],
    ids=[
        'flat_file1.json - flat_file2.json',
        'flat_file1.yml - flat_file2.yml',
        'nested_file1.json - nested_file2.json',
        'nested_file1.yml - nested_file2.yml'
    ],
)
def test_generate_diff(filepath1, filepath2, output):
    assert generate_diff(filepath1, filepath2) == output
