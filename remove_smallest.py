def remove_smallest(numbers):
    a = numbers[:]
    if a:
        a.remove(min(a))
    return a


print(remove_smallest([1, 2, 3, 1, 1]))