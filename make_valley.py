def make_valley(arr):
    lst = sorted(arr)
    if len(lst)% 2 == 1:
        center = [lst.pop(0)]
    else:
        center = []
    left = []
    right = []
    for idx in range(0,len(lst)):
        if idx % 2 == 0:
            right.append(lst[idx])
        else:
            left.append(lst[idx])
    left.sort(reverse=True)
    return left + center + right

print(make_valley([17, 17, 15, 14, 8, 7, 7, 5, 4, 4, 1, 1]))