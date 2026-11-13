import json


def load_benchmark(path):
    with open(path, 'r', encoding='utf-8') as fh:
        return [json.loads(line) for line in fh]
