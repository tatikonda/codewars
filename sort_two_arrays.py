def sort_two_arrays(arr1, arr2):
    a1 = sorted((x, i) for i, x in enumerate(arr1))
    a2 = sorted((x, i) for i, x in enumerate(arr2))
    return [[arr1[i] for i in [x[1] for x in a2]], [arr2[i] for i in [x[1] for x in a1]]]

print(sort_two_arrays([5,4,3,2,1], [6,5,7,8,9]))