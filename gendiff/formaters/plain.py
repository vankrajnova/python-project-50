def make_plain(diff, path=''):
    def parse_value(value):
        if isinstance(value, dict):
            return "[complex value]"
        else:
            if type(value) is bool:
                return f"{value}".lower()
            elif value is None:
                return "null"
            else:
                return f"'{value}'"

    def make_str_for_unchanged():
        return ""

    def make_str_for_added(key, value):
        if isinstance(value, dict):
            return f"""\nProperty '{key}' was added with value: {parse_value(value)}"""
        else:
            return f"""\nProperty '{key}' was added with value: {parse_value(value)}"""

    def make_str_for_removed(key):
        return f"\nProperty '{key}' was removed"

    def make_str_for_updated(key, old_value, value):
        result = f"\nProperty '{key}' was updated. "
        result += f"From {parse_value(old_value)} to {parse_value(value)}"
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
