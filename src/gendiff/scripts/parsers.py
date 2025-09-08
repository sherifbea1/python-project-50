import json
import yaml
import os


def parse_file(filepath):
    extension = os.path.splitext(filepath)[1]

    with open(filepath) as f:
        if extension in ['.yml', '.yaml']:
            return yaml.safe_load(f)
        elif extension == '.json':
            return json.load(f)
        else:
            raise ValueError(f"Unsupported file format: {extension}")
