from json import dumps


def _parse_value(value) -> str:
    if isinstance(value, dict):
        return "[complex value]"
    if any(
        (type(value) is bool, isinstance(value, int), value is None)
    ):
        return value if isinstance(value, str) else dumps(value)
    return f"'{value}'"


def _make_str(
        action: str, path: str, value: str, old_value: str | None = None
) -> str:
    map_dict = {
        "removed": "was removed\n",
        "updated": f"was updated. "
                   f"From {_parse_value(old_value)} to {_parse_value(value)}\n",
        "added": f"was added with value: {_parse_value(value)}\n"
    }

    result = ''

    for key, value in map_dict.items():
        if key == action:
            if action != 'unchanged':
                result += f"Property '{path}' {value}"
    return result


def make_plain(diff: dict, path: str = '') -> str:
    result = ''
    for key, value in sorted(diff.items()):
        key = f'{path}.{key}' if path else key

        result += ''

        if 'children' in value:
            result += make_plain(value['children'], f'{key}')
        else:
            old = value['old_value'] if value['action'] == 'updated' else None
            result += _make_str(
                action=value['action'],
                value=value['value'],
                old_value=old,
                path=key
            )
    return result
