from gendiff.diff import build_diff
from gendiff.formaters.stylish import make_stylish
from gendiff.load_data import load


def _choose_format(format_name: str):
    if format_name == 'stylish':
        return make_stylish


def generate_diff(first_file, second_file, format_name='stylish'):
    file1 = load(first_file)
    file2 = load(second_file)

    diff = build_diff(file1, file2)
    output_format = _choose_format(format_name)
    return output_format(diff)
