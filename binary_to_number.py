def binary_array_to_number(arr):
    return int(''.join([str(item) for item in arr]), 2)

def binary_array_to_number(arr):
    s = 0
    for digit in arr:
        s = s * 2 + digit

    return s
print(binary_array_to_number([0,0,0,1]))