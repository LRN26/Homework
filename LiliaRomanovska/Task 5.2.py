def most_common_words(filepath, number_of_words=3):
    """function which search for most common words in the file"""

    all_words = {}
    with open(filepath, 'r') as input_file:
        list_of_words = input_file.read().lower().split()
        for word in list_of_words:
            if not word.isalpha():
                word = "".join([i for i in word if i.isalpha()])
            all_words[word] = all_words.get(word, 0) + 1
    list_of_words = sorted(all_words, key=all_words.get, reverse=True)[:number_of_words]

    return list_of_words


print(most_common_words(r'C:\Users\Lenovo\Downloads\data\lorem_ipsum.txt', 3))
