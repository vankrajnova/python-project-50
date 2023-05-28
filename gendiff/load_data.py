import json
import yaml


def load(file_name: str) -> dict:
    if file_name.endswith('.json'):
        return json.load(open(file_name))
    elif file_name.endswith('.yml') or file_name.endswith('.yaml'):
        return yaml.safe_load(open(file_name))
    else:
        raise Exception(
            'Unknown file format! Available formats: yml, yaml, json'
        )
