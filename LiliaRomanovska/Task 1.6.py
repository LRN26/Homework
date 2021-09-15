t_nums = (1, 2, 3, 4)


def tuple_int(t_nums):
    tuple_changed = map(str, t_nums)
    nums_int = int(''.join(tuple_changed))
    return nums_int


print(tuple_int(t_nums))
