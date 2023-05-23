import json
import pytest

from gendiff import generate_diff
from tests import FIXTURES_PATH


#
#
# @pytest.fixture
# def open_files():
#     file1 = json.load(open('tests/fixtures/file1.json'))
#     file2 = json.load(open('tests/fixtures/file2.json'))
#     return file1, file2


def test_if_key_in_both_files():
    with open(f'{FIXTURES_PATH}expected_result.txt') as f:
        expected_str = f.read()
    print(generate_diff(f'{FIXTURES_PATH}file1.yml', f'{FIXTURES_PATH}file2.yml'))
    assert generate_diff(f'{FIXTURES_PATH}file1.yml', f'{FIXTURES_PATH}file2.yml') == expected_str
