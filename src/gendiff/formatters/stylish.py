def format_value(value, depth):
    if isinstance(value, dict):
        indent = '    ' * (depth + 1)
        lines = ['{']
        for k, v in value.items():
            lines.append(f"{indent}{k}: {format_value(v, depth + 1)}")
        lines.append('    ' * depth + '}')
        return '\n'.join(lines)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def stylish(diff, depth=1):
    indent = '    ' * depth
    sign_indent = '  ' + '    ' * (depth - 1)
    result = ['{']

    for node in diff:
        key = node['key']
        status = node['status']

        if status == 'nested':
            children = stylish(node['children'], depth + 1)
            result.append(f"{indent}{key}: {children}")

        elif status == 'unchanged':
            value = format_value(node['value'], depth)
            result.append(f"{indent}{key}: {value}")

        elif status == 'removed':
            value = format_value(node['value'], depth)
            result.append(f"{sign_indent}- {key}: {value}")

        elif status == 'added':
            value = format_value(node['value'], depth)
            result.append(f"{sign_indent}+ {key}: {value}")

        elif status == 'updated':
            old_value = format_value(node['old_value'], depth)
            new_value = format_value(node['new_value'], depth)
            result.append(f"{sign_indent}- {key}: {old_value}")
            result.append(f"{sign_indent}+ {key}: {new_value}")

    result.append('    ' * (depth - 1) + '}')
    return '\n'.join(result)
