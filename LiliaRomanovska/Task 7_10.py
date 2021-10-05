def endless_generator():

    """Function implements a generator which will generate odd numbers endlessly."""

    start = 1
    while True:
        yield start
        start += 2


def main():
    gen = endless_generator()
    while True:
        print(next(gen), end=" ")


if __name__ == "__main__":
    main()
