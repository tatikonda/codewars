def stray(arr):
    for x in arr:
        if arr.count(x) == 1:
            return x

print(stray([3,2,2,2,2]))