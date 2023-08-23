INDENT = '    '
ADD = '  + '
REMOVE = '  - '
OPEN_BRACE = '{\n'
CLOSE_BRACE = '}\n'


def to_str(item, depth: int) -> str:
    if isinstance(item, dict):
        result = OPEN_BRACE
        for key, value in item.items():
            if isinstance(value, dict):
                upd_value = to_str(value, depth + 1)
                result += f'{INDENT * depth}{INDENT}{key}:' \
                          f' {upd_value}\n'
            else:
                result += f'{INDENT * depth}{INDENT}{key}:' \
                          f' {value}\n'
        result += f'{INDENT * depth}{CLOSE_BRACE}'
        return result.strip()
    if isinstance(item, bool):
        return str(item).lower()
    if item is None:
        return 'null'
    return item


def make_stylish(tree: dict) -> str:
    def walk(node, depth):
        result = OPEN_BRACE
        for key, value in sorted(node.items()):
            cur_depth = depth + 1
            if 'children' in value:
                result += f'{INDENT * cur_depth}{key}:' \
                          f' {walk(value.get("children"), cur_depth)}\n'
            else:
                new_value = value.get('value')
                old_value = value.get('old_value')
                actions = {
                    'updated': f'{INDENT * depth}'
                               f'{REMOVE}{key}: '
                               f'{to_str(old_value, cur_depth)}\n'
                               f'{INDENT * depth}'
                               f'{ADD}{key}: '
                               f'{to_str(new_value, cur_depth)}\n',
                    'added': f'{INDENT * depth}'
                             f'{ADD}{key}: '
                             f'{to_str(new_value, cur_depth)}\n',
                    'removed': f'{INDENT * depth}'
                               f'{REMOVE}{key}: '
                               f'{to_str(new_value, cur_depth)}\n',
                    'unchanged': f'{INDENT * depth}'
                                 f'{INDENT}{key}: '
                                 f'{to_str(new_value, cur_depth)}\n'
                }
                result += actions[value.get('action')]
        result += f'{INDENT * depth}{CLOSE_BRACE}'
        return result.strip()

    return walk(tree, 0)
