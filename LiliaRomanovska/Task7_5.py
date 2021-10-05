class WrongType(Exception):
    pass


class NumberNotGreaterThanTwo(Exception):
    pass


class IsNotEvenError(Exception):
    pass


def number_checking(num):

    """
        function for check that number is even and is greater than 2.
        Throw different exceptions for this errors.
        Custom exceptions must be derived from custom base exception(not Base Exception class).
    """
    
    if isinstance(num, float):
        raise WrongType('Number is not an integer')
    if num <= 2:
        raise NumberNotGreaterThanTwo('Number is too small')
    if num % 2 != 0:
        raise IsNotEvenError('Number must be even')
    return num


def main():
    number_checking(4)


if __name__ == "__main__":
    main()
