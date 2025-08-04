import json
import argparse


def format_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    else:
        return str(value)


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    keys = sorted(set(data1.keys()) | set(data2.keys()))
    lines = []

    for key in keys:
        if key in data1 and key not in data2:
            lines.append(f"  - {key}: {format_value(data1[key])}")
        elif key not in data1 and key in data2:
            lines.append(f"  + {key}: {format_value(data2[key])}")
        elif data1[key] == data2[key]:
            lines.append(f"    {key}: {format_value(data1[key])}")
        else:
            lines.append(f"  - {key}: {format_value(data1[key])}")
            lines.append(f"  + {key}: {format_value(data2[key])}")

    return '{\n' + '\n'.join(lines) + '\n}'


def main():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file))
