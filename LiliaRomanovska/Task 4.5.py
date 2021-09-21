def split_by_index(num: int):
    """function returns a tuple of a given integer's digits."""

    num_str = str(num)
    get_digits = tuple(int(i) for i in num_str)
    return get_digits


print(split_by_index(87178291199))
