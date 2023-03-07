def parse_priority(value):
    value_int = ord(value)

    if value_int < 91:
        return value_int - 38

    return value_int - 96
