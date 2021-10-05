from Task7_5 import number_checking, WrongType, NumberNotGreaterThanTwo, IsNotEvenError


def prime_number(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def goldbach():

    """function  for proving Goldbach's conjecture. Program accepts number for input and print result."""

    while True:
        num_input = input("Enter an even number greater than 2 or 'q' to quit: ")
        if num_input == "q":
            print("Exit!")
            return None

        try:
            number = int(num_input)
            if not number_checking(number):
                continue

            for i in range(1, number):
                j = number - i
                if prime_number(i) and prime_number(j):
                    print(f"{number} = {i} + {j}\n")
                    break

        except WrongType:
            print("Number is not an integer")
        except IsNotEvenError:
            print("Number must be even")
        except NumberNotGreaterThanTwo:
            print("Number is too small")
        else:
            goldbach()


def main():
    goldbach()


if __name__ == "__main__":
    main()
