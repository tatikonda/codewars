def is_nice(arr):
    for x in arr:
        if x + 1 not in arr and x - 1 not in arr:
            return False
    return True and len(arr) > 0

print(is_nice([2,10,9,3]))