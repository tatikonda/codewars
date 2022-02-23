def gimme(input_array):
    sorted_list = sorted(input_array)
    return input_array.index(sorted_list[1])

print(gimme([5, 10, 14]))