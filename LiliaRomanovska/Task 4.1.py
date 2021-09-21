def replace_symbols(string_in):
    """a function receives a string and replaces all `"` symbols
    with `'` and vise versa."""

    string_out = ""

    for i in string_in:
        if i == '"':
            string_out += "'"
        elif i == "'":
            string_out += '"'
        else:
            string_out += i
    return string_out


print(replace_symbols('"I’ll start learning Python soon," said Steven'))
