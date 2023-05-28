from gendiff.diff import build_diff
from gendiff.formaters.json import make_json
from gendiff.formaters.plain import make_plain
from gendiff.formaters.stylish import make_stylish
from gendiff.load_data import load


def generate_diff(first_file, second_file, formatter='stylish'):
    file1 = load(first_file)
    file2 = load(second_file)

    diff = build_diff(file1, file2)
    if formatter == 'stylish':
        return make_stylish(diff)
    elif formatter == 'plain':
        return make_plain(diff)[:-1]
    elif formatter == 'json':
        return make_json(diff)
