def test_1_1(*args):
    """function receives a changeable number of strings and return
    characters that appear in all strings"""

    import string
    all_characters = set(string.ascii_lowercase)
    for i in args:
        all_characters = all_characters.intersection(set(i))

    return all_characters


print(test_1_1("hello", "world", "python",))


def test_1_2(*args):
    """functions which receive a changeable number of strings and return
    characters that appear in at least one string"""

    single_characters = set()

    for string in args:
        single_characters.update(set(string))

    return single_characters


print(test_1_2("hello", "world", "python",))


def test_1_3(*args):
    """functions which receive a changeable number of strings and return
    characters that appear at least in two strings"""

    appear_in_two_strings = set()
    for i in range(len(args) - 1):
        for j in range(i + 1, len(args)):
            single_characters = set(args[i]).intersection(set(args[j]))
            appear_in_two_strings.update(single_characters)

    return appear_in_two_strings


print(test_1_3("hello", "world", "python",))


def test_1_4(*args):
    """functions which receive a changeable number of strings and return
    characters of alphabet, that were not used in any string"""

    import string
    characters_not_used = set(string.ascii_lowercase)
    for i in args:
        characters_not_used\
            .difference_update(set(i))

    return (characters_not_used)


print(test_1_4("hello", "world", "python",))
