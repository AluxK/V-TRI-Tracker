# Converts an array of characters into a string.
def convert_chr_to_string(chr_array):
    temp_string = ""

    for x in chr_array:
        temp_string += x
    return temp_string


# Gets a set of numbers from a string.
def get_numbers_from_string(filename):
    num_array = []

    # checks each character of a string to check if it's a number and if it is, it is added to an array
    x = 0
    is_digit = True
    while is_digit:
        if filename[x].isdigit():
            num_array.append(filename[x])
            x += 1
        else:
            is_digit = False
    return num_array
