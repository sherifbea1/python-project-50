from gendiff.parsers import parse_file
from gendiff.formatters.stylish import stylish

FORMATTERS = {
    'stylish': stylish,
}


def build_diff(data1, data2):
    if not isinstance(data1, dict) or not isinstance(data2, dict):
        raise TypeError('Ожидались словари для сравнения')

    keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in keys:
        if key not in data2:
            diff.append({'key': key, 'status': 'removed', 'value': data1[key]})
        elif key not in data1:
            diff.append({'key': key, 'status': 'added', 'value': data2[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                'key': key,
                'status': 'nested',
                'children': build_diff(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            diff.append({'key': key, 'status': 'unchanged', 'value': data1[key]})
        else:
            diff.append({
                'key': key,
                'status': 'updated',
                'old_value': data1[key],
                'new_value': data2[key]
            })

    return diff


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)

    formatter = FORMATTERS.get(format_name)
    if not formatter:
        raise ValueError(f"Неизвестный формат: {format_name}")

    return formatter(diff)
