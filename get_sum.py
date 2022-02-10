def get_sum(a,b):
    total = 0
    if a == b:
        return a
    for i in range(min(a,b), max(a,b)+1):
        print(i)
        total += i
    return total

print(get_sum(0,-1))