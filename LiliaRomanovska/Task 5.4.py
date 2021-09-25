"""1.way to call "inner_function" without moving it from inside of "enclosed_function."""

a = "I am global variable!"


def enclosed_function_1():
    a = "I am variable from enclosed function!"

    def inner_function():
        a = "I am local variable!"
        print(a)

    return inner_function


"""2.Modify ONE LINE in `inner_function` to make it print variable 'a' from global scope."""

a = "I am global variable!"


def enclosed_function_2():
    a = "I am variable from enclosed function!"

    def inner_function():
        global a
        print(a)

    return inner_function


"""3. Modify ONE LINE in `inner_function` to make it print variable 'a' form enclosing function."""

a = "I am global variable!"


def enclosed_function_3():
    a = "I am variable from enclosed function!"

    def inner_function():
        nonlocal a
        print(a)

    return inner_function
