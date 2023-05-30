def _make_dict(
        action: str, value: str, old_value: str | None = None,
) -> dict:
    map_dict = {
        'updated': {
            'action': 'updated',
            'old_value': old_value,
            'value': value
        },
        'unchanged': {
            'action': 'unchanged',
            'value': value
        },
        'added': {
            'action': 'added',
            'value': value
        },
        'removed': {
            'action': 'removed',
            'value': value
        }
    }
    for key, value in map_dict.items():
        if key == action:
            return value


def build_diff(data1: dict, data2: dict) -> dict:
    result = {}

    for key in set(data1) | set(data2):
        if key in data1 and key in data2:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result[key] = {'children': build_diff(data1[key], data2[key])}
            else:
                if data1[key] != data2[key]:
                    result[key] = _make_dict(
                        'updated', old_value=data1[key], value=data2[key]
                    )
                else:
                    result[key] = _make_dict('unchanged', data1[key])

        elif key in data1:
            result[key] = _make_dict('removed', data1[key])
        else:
            result[key] = _make_dict('added', data2[key])

    return result
