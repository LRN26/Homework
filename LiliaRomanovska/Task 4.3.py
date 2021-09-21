def str_split(sentence: str):
    """function which works the same as `str.split` method"""

    list_1 = []
    word = ''

    for i in sentence:
        if i != ' ':
            word += str(''.join(i))
        else:
            list_1.append(word)
            word = ''
    list_1.append(word)
    return list_1


print(str_split('hello my dear friend'))

