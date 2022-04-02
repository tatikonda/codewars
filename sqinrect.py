def sqInRect(a, b):
    if a == b:
        return None
    res = []
    while b:
        b, a = sorted([a, b])
        res += [b]
        a, b = b, a-b    
    return res

print(sqInRect(5,3))