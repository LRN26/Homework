def suppress_exceptions(func):

    """Implement decorator for suppressing exceptions. If exception not occurs write log to console."""

    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            print("There is a problem")

    return wrapper


@suppress_exceptions
def divide(x, y):
    print(x / y)


def main():
    divide(1, 0)


if __name__ == "__main__":
    main()
