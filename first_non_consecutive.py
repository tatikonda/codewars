def first_non_consecutive(arr):
    prev = arr[0]
    first = None
    for num in arr[1:]:
        if (prev + 1) != num:
            first = num
            break
        prev += 1
    return first


print(first_non_consecutive([1,2,3,5,6,7,8]))

