def sum_dig_pow(a, b):
    res = []
    for i in range(a, b+1):
        total_sum = sum(int(x) ** (index + 1) for index, x in enumerate(str(i)))
        if total_sum == i:
            res.append(i)
    return res

def sum_dig_pow(a, b):
    return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]
    
print(sum_dig_pow(1, 100))
