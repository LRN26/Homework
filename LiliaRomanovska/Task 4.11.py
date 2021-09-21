def combine_dicts(*args):
    """"function receives changeable number of dictionaries (keys - letters, values - numbers)
    and combines them into one dictionary. Dict values are summarized in case of identical keys"""

    dict_out = {}

    for dict_in in args:
        for key in dict_in:
            if key in dict_out:
                dict_out[key] += dict_in[key]
            else:
                dict_out.update({key: dict_in[key]})

    return dict_out


dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}
print(combine_dicts(dict_1, dict_2))
print(combine_dicts(dict_1, dict_2, dict_3))
