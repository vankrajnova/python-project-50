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


def _make_dict(
        action: str, key: str, value: str, old_value: str | None = None
) -> dict:
    map_dict = {
        'added': {f'+ {key}': value},
        'removed': {f'- {key}': value},
        'updated': {f'- {key}': old_value,
                    f'+ {key}': value},
        'unchanged': {key: value}
    }
    for key, value in map_dict.items():
        if key == action:
            return value


def make_stylish(diff: dict) -> str:
    def walk(diff):
        result = {}

        for key, value in sorted(diff.items()):
            if 'children' in value:
                result[key] = walk(value['children'])
            else:
                action = value['action']
                old = value['old_value'] if action == 'updated' else None
                result.update(
                    _make_dict(action, key, value['value'], old)
                )

        return result

    result = json.dumps(walk(diff), indent=4)
    return _convert_string(result)
