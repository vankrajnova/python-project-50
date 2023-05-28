def _parse_value(value: str | dict) -> str:
    if isinstance(value, dict):
        return "[complex value]"
    else:
        if type(value) is bool:
            return f"{value}".lower()
        elif value is None:
            return "null"
        else:
            return f"'{value}'"


def make_plain(diff: dict, path: str = '') -> str:
    def make_str_for_unchanged():
        return ""

    def make_str_for_added(key, value):
        return f"Property '{key}' was added with value: {_parse_value(value)}\n"

    def make_str_for_removed(key):
        return f"Property '{key}' was removed\n"

    def make_str_for_updated(key, old_value, value):
        result = f"Property '{key}' was updated. "
        result += f"From {_parse_value(old_value)} to {_parse_value(value)}\n"
        return result

    result = ''
    for key, value in sorted(diff.items()):
        key = f'{path}.{key}' if path else key
        if 'children' in value:
            result += make_plain(value['children'], f'{key}')
        elif 'unchanged' in value:
            result += make_str_for_unchanged()
        elif 'added' in value:
            result += make_str_for_added(key, value["added"])
        elif 'removed' in value:
            result += make_str_for_removed(key)
        elif 'old_value' in value:
            result += make_str_for_updated(key, value["old_value"], value["new_value"])
    return result
