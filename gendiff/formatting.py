from gendiff.formaters.json import make_json
from gendiff.formaters.plain import make_plain
from gendiff.formaters.stylish import make_stylish


def formatting(diff: dict, formatter: str):
    if formatter == 'stylish':
        return make_stylish(diff)
    elif formatter == 'plain':
        return make_plain(diff)[:-1]
    elif formatter == 'json':
        return make_json(diff)
    else:
        raise Exception(
            'Unknown format! Available formats: stylish, plain, json'
        )
