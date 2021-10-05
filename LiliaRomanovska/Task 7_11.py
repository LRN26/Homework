def endless_fib_generator():

    """
        Function implements a generator which will geterate [Fibonacci numbers] endlessly.
    """
    a = 0
    b = 1
    while True:
        yield a
        a = b
        b = a+b


def main():
    gen = endless_fib_generator()
    while True:
        print(next(gen), end=" ")


if __name__ == "__main__":
    main()
