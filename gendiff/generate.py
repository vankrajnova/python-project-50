import json
import yaml


def _sort_by_element(element: str):
    return element[4]


def open_file(first_file: str, second_file: str):
    if first_file.endswith('.json') and second_file.endswith('.json'):
        file1 = json.load(open(first_file))
        file2 = json.load(open(second_file))
    else:
        file1 = yaml.safe_load(open(first_file))
        file2 = yaml.safe_load(open(second_file))

    return file1, file2


def generate_diff(first_file, second_file):
    file1, file2 = open_file(first_file, second_file)

    compare_list = []

    intersection = set(file1) & set(file2)
    difference_f1_f2 = set(file1) - set(file2)
    difference_f2_f1 = set(file2) - set(file1)

    for el in intersection:
        if file1[el] == file2[el]:
            compare_list.append(f'    {el}: {file1[el]}')
        elif file1[el] != file2[el]:
            compare_list.append(f'  - {el}: {file1[el]}')
            compare_list.append(f'  + {el}: {file2[el]}')

    for el in difference_f1_f2:
        compare_list.append(f'  - {el}: {file1[el]}')

    for el in difference_f2_f1:
        compare_list.append(f'  + {el}: {file2[el]}')

    compare_str = '\n'.join(sorted(compare_list, key=_sort_by_element)).lower()
    return '{\n' + compare_str + '\n}'
