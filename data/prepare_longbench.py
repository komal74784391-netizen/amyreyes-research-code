from datasets import load_dataset


def build_splits(path):
    return load_dataset('json', data_files=path)
