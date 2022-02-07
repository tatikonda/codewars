def sum_array(arr):
    if arr == '' or arr is None or len(arr) == 1:
        return 0
    result = sum(sorted(arr)[1:-1])
    return result

print(sum_array([6, 2, 1, 8, 10]))