def camel_case_to_snake_case(text: str, prefix: str = "") -> str:
    parts = []
    if prefix:
        parts.append(prefix)

    part = ""
    char: str
    for not_first, char in enumerate(text):
        if char.isupper():
            if not_first:
                parts.append(part)
            part = char.lower()
        else:
            part += char
    parts.append(part)  # last one
    return "_".join(parts)
