"""Implement a decorator `call_once` which runs a function or method once and caches the result.
All consecutive calls to this function should return cached result no matter the arguments."""

def call_once(func):
    cached_res = 0

    def wrapper(a, b):
        nonlocal cached_res
        if cached_res == 0:
            cached_res = func(a, b)
        return cached_res

    return wrapper

@call_once
def sum_of_numbers(a, b):
    return a + b

print(sum_of_numbers(13, 42))
print(sum_of_numbers(999, 100))
print(sum_of_numbers(134, 412))
print(sum_of_numbers(856, 232))
