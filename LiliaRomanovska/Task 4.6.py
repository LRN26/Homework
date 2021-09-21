def get_longest_word(string_in):
    """Function get_longest_word(input_string: string) -> longest_word: string
    returns the longest word in the given string."""

    import string

    excluded = set(string.punctuation)
    my_string = ''.join(i for i in string_in if i not in excluded)
    my_list = my_string.split()
    longest_word = max(my_list, key=len)
    return longest_word


print(get_longest_word('Python is simple and effective!'))
