def generate_squares(number):
    """a function takes a number as an argument and returns a dictionary, 
    where the key is a number, the value is the square of that number."""

    dict_out = {}
    for i in range(1, number+1):
        dict_out[i] = i*i
    return dict_out


print(generate_squares(6))