from gendiff.diff import build_diff
from gendiff.formaters.plain import make_plain
from gendiff.formaters.stylish import make_stylish
from gendiff.load_data import load


def _choose_format(formatter: str):
    if formatter == 'stylish':
        return make_stylish
    elif formatter == 'plain':
        return make_plain


def generate_diff(first_file, second_file, formatter='stylish'):
    file1 = load(first_file)
    file2 = load(second_file)

    diff = build_diff(file1, file2)
    output_format = _choose_format(formatter)
    return output_format(diff).strip()
