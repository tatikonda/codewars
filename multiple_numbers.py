def multiple_of_index(arr):
    res = []
    for i,n in enumerate(arr):
        if i > 0:
            if n % i == 0:
                res.append(n)
    return res

print(multiple_of_index([22, -6, 32, 82, 9, 25]))