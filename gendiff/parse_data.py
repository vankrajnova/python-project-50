import json
import yaml


def parse(data, format_name):
    FORMATS = {
        'json': json.loads,
        'yaml': yaml.safe_load,
        'yml': yaml.safe_load
    }

    return FORMATS.get(format_name)(data)
