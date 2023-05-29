def build_diff(data1: dict, data2: dict) -> dict:
    def make_common_by(key):
        if isinstance(data1[key], dict) and isinstance(data2[key], dict):
            return {
                'children': build_diff(data1[key], data2[key])
            }
        elif data1[key] != data2[key]:
            return {
                'action': 'updated',
                'old_value': data1[key],
                'value': data2[key]
            }
        else:
            return {
                'action': 'unchanged',
                'value': data1[key]
            }

    def make_added_by(key):
        return {
            'action': 'added',
            'value': data2[key]
        }

    def make_removed_by(key):
        return {
            'action': 'removed',
            'value': data1[key]
        }

    result = {}
    for key in set(data1) | set(data2):
        if key in data1 and key in data2:
            handler = make_common_by
        elif key in data1:
            handler = make_removed_by
        else:
            handler = make_added_by
        result[key] = handler(key)
    return result


