import json


def _convert_string(string: str) -> str:
    data = {
        '"': '',
        ',': '',
        '   +': ' +',
        '   -': ' -',
        '"true"': 'true',
        '"false"': 'false',
        '"null"': 'null',
    }
    for key, value in data.items():
        string = string.replace(key, value)
    return string


def make_stylish(diff: dict) -> str:
    def walk(diff):
        result = {}

        for key, value in sorted(diff.items()):
            if 'children' in value:
                result[key] = walk(value['children'])
            elif 'old_value' in value:
                result[f'- {key}'] = value['old_value']
                result[f'+ {key}'] = value['new_value']
            elif 'unchanged' in value:
                result[key] = value['unchanged']
            elif 'added' in value:
                result[f'+ {key}'] = value['added']
            elif 'removed' in value:
                result[f'- {key}'] = value['removed']
        return result

    result = json.dumps(walk(diff), indent=4)
    return _convert_string(result)
