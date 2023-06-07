from gendiff.diff import build_diff
from gendiff.formatting import formatting
from gendiff.parse_data import parse


def generate_diff(first_file, second_file, formatter='stylish'):
    file1 = parse(file_path=first_file)
    file2 = parse(file_path=second_file)

    diff = build_diff(file1, file2)
    return formatting(diff, formatter)
