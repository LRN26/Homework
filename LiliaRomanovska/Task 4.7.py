def foo(lst_in):
    """a function, which given a list of
    integers, return a new list such that each element at index `i` of the new list
    is the product of all the numbers in the original array except the one at `i`."""

    import numpy as np
    lst_out = []
    for i in range(len(lst_in)):
        lst_out.append(int(np.prod(lst_in) / lst_in[i]))
    return lst_out


print(foo([1, 2, 3, 4, 5]))
