def cube_odd(arr):
    total = 0 
    for num in arr:
        if (type(num) != int):
            return None
        if num % 2 != 0:
            total += num**3
    return total

print(cube_odd(["a",12,9,"z",42]))