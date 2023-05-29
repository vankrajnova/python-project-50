import pytest
from gendiff import generate_diff
from gendiff.diff import build_diff
from gendiff.formaters.plain import make_plain
from gendiff.load_data import load
from tests import FIXTURES_DIR


def _get_expected_output_by(file_name: str) -> str:
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
FLAT_STYLISH_OUTPUT = _get_expected_output_by('flat_output.txt')
NESTED_STYLISH_OUTPUT = _get_expected_output_by('nested_output.txt')
FLAT_JSON_OUTPUT = _get_expected_output_by('flat_json_output.json')
NESTED_JSON_OUTPUT = _get_expected_output_by('nested_json_output.json')
PLAIN_OUTPUT = _get_expected_output_by('plain_output.txt')


@pytest.mark.parametrize(
    'filepath1, filepath2, output, formatter',
    [
        (JSON1, JSON2, FLAT_STYLISH_OUTPUT, 'stylish'),
        (YAML1, YAML2, FLAT_STYLISH_OUTPUT, 'stylish'),
        (NESTED_JSON1, NESTED_JSON2, NESTED_STYLISH_OUTPUT, 'stylish'),
        (NESTED_YAML1, NESTED_YAML2, NESTED_STYLISH_OUTPUT, 'stylish'),
        (NESTED_JSON1, NESTED_JSON2, PLAIN_OUTPUT, 'plain'),
        (NESTED_YAML1, NESTED_YAML2, PLAIN_OUTPUT, 'plain'),
        (JSON1, JSON2, FLAT_JSON_OUTPUT, 'json'),
        (NESTED_JSON1, NESTED_JSON2, NESTED_JSON_OUTPUT, 'json'),
    ],
    ids=[
        'data=two flat json, format=stylish',
        'data=two flat yml, format=stylish',
        'data=two nested json, format=stylish',
        'data=two nested yml, format=stylish',

        'data=two nested json, format=plain',
        'data=two nested yml, format=plain',

        'data=two flat json, format=json',
        'data=two nested json, format=json'
    ],
)
def test_generate_diff(filepath1, filepath2, output, formatter):
    assert generate_diff(filepath1, filepath2, formatter) == output


def test():
    diff = build_diff(load(NESTED_JSON1), load(NESTED_JSON2))
    # print(diff)
    print(make_plain(diff))
    make_plain(diff)
    # action = "updated"
    # value = 1
    # old_value = 0
    #
    # d = {
    #     "unchanged": "",
    #     "removed": "was removed\n",
    #     "updated": f"was updated. From {old_value} to {value})\n",
    #     "added": f"was added with value: {value}\n"
    # }
    # s = ''
    # for key, value in d.items():
    #     if key == action:
    #         print('s')
    #         s += value
    # print(s)
