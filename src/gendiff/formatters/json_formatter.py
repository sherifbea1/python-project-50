# src/gendiff/formatters/json_formatter.py
import json


def json_formatter(diff):
    return json.dumps(diff, indent=4)
