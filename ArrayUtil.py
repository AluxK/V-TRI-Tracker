# finds the index of the highest value in an array of numbers
def find_index_of_highest_value(array):
    new_index = 0
    highest_value_index = 0

    for value in array:
        if array[highest_value_index] <= value:
            highest_value_index = new_index
        new_index += 1
    return highest_value_index
