from gendiff.diff import build_diff
from gendiff.formatting import formatting
from gendiff.parse_data import parse


def generate_diff(first_file, second_file, format_name='stylish'):
    first_data, first_format = read_file(first_file)
    second_data, second_format = read_file(second_file)

    first_dict = parse(first_data, first_format)
    second_dict = parse(second_data, second_format)

    diff = build_diff(first_dict, second_dict)
    return formatting(diff, format_name)


def read_file(file_name):
    with open(file_name, 'r') as file:
        file_data = file.read()
        file_format = file_name.split('.')[-1]
        return file_data, file_format
