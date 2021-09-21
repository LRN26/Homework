def get_pairs(lst_in: list):
    """a function returns a list
    of tuples containing pairs of neighbor elements."""

    if len(lst_in) <= 1:
        return None

    lst_out = []
    for i in range(len(lst_in) - 1):
        lst_out.append((lst_in[i], lst_in[i + 1]))
    return lst_out


print(get_pairs([1, 2, 3, 8, 9]))
