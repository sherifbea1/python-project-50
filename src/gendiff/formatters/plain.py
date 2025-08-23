def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'"
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)


def walk(diff, path=""):
    lines = []
    for node in diff:
        key = node["key"]
        property_path = f"{path}{key}"
        status = node["status"]

        if status == "nested":
            lines.extend(walk(node["children"], property_path + "."))
        elif status == "added":
            value = format_value(node["value"])
            lines.append(f"Property '{property_path}' was added with value: {value}")
        elif status == "removed":
            lines.append(f"Property '{property_path}' was removed")
        elif status == "updated":
            old_value = format_value(node["old_value"])
            new_value = format_value(node["new_value"])
            lines.append(
                f"Property '{property_path}' was updated. "
                f"From {old_value} to {new_value}"
)

    return lines


def plain(diff):
    return "\n".join(walk(diff))
