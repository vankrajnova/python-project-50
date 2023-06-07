import json
import yaml


def _get_end_point(file_path: str) -> str:
    name = file_path.split('/')[-1]
    return name.split('.')[-1]


def _get_data(file_path: str) -> str:
    with open(file_path, 'r') as f:
        data = f.read()
    return data


def _read_file(file_path: str) -> tuple:
    data = _get_data(file_path)
    end_point = _get_end_point(file_path)
    return data, end_point


def parse(
        file_path: str = None, end_point: str = None, data: str = None,
):
    if file_path:
        data, end_point = _read_file(file_path)

    if end_point == 'json':
        return json.loads(data)
    elif end_point == 'yaml' or end_point == 'yml':
        return yaml.safe_load(data)
    else:
        raise Exception(
            'Unknown file format! Available formats: yml, yaml, json'
        )
