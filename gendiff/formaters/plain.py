def serialize(value):
    match value:
        case True:
            return 'true'
        case False:
            return 'false'
        case None:
            return 'null'
        case _:
            return value


def stringify(value):
    if type(value) is int:
        return serialize(value)
    if type(value) is str:
        return f"'{serialize(value)}'"
    if type(value) is dict:
        return '[complex value]'
    return f'{serialize(value)}'


def _make_str(
        action: str, path: str, value: str, old_value: str | None = None
) -> str:
    map_dict = {
        "removed": "was removed\n",
        "updated": f"was updated. "
                   f"From {stringify(old_value)} to {stringify(value)}\n",
        "added": f"was added with value: {stringify(value)}\n"
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
