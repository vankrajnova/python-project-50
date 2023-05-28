import json


def make_json(diff: dict) -> json:
    return json.dumps(diff, indent=4, sort_keys=True)
