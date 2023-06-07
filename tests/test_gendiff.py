import pytest
from gendiff import generate_diff
from tests import FIXTURES_DIR


def _get_expected_output_by(file_name: str) -> str:
    with open(f'{FIXTURES_DIR}{file_name}') as f:
        expected_str = f.read()
    return expected_str


def _get_file_path_by(file_name: str) -> str:
    return f'{FIXTURES_DIR}{file_name}'


NESTED_JSON1 = _get_file_path_by('nested_file1.json')
NESTED_JSON2 = _get_file_path_by('nested_file2.json')
NESTED_YAML1 = _get_file_path_by('nested_file1.yml')
NESTED_YAML2 = _get_file_path_by('nested_file2.yml')
NESTED_STYLISH_OUTPUT = _get_expected_output_by('nested_output.txt')
NESTED_JSON_OUTPUT = _get_expected_output_by('nested_json_output.json')
PLAIN_OUTPUT = _get_expected_output_by('plain_output.txt')


@pytest.mark.parametrize(
    'filepath1, filepath2, output, formatter',
    [
        (NESTED_JSON1, NESTED_JSON2, NESTED_STYLISH_OUTPUT, 'stylish'),
        (NESTED_YAML1, NESTED_YAML2, NESTED_STYLISH_OUTPUT, 'stylish'),
        (NESTED_JSON1, NESTED_JSON2, PLAIN_OUTPUT, 'plain'),
        (NESTED_YAML1, NESTED_YAML2, PLAIN_OUTPUT, 'plain'),
        (NESTED_JSON1, NESTED_JSON2, NESTED_JSON_OUTPUT, 'json'),
    ],
    ids=[
        'data=two nested json, format=stylish',
        'data=two nested yml, format=stylish',

        'data=two nested json, format=plain',
        'data=two nested yml, format=plain',

        'data=two nested json, format=json'
    ],
)
def test_generate_diff(filepath1, filepath2, output, formatter):
    assert generate_diff(filepath1, filepath2, formatter) == output
