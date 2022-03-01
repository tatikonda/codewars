def capitalize(s):
    res1 = ''
    res2 = ''
    for i, j in enumerate(s):
        if i % 2 == 0:
            res1 += j.upper()
        else:
            res1 += j
        if i % 2 != 0:
            res2 += j.upper()
        else:
            res2 += j
    return [res1, res2]

def capitalize(s):
    s = ''.join(c if i%2 else c.upper() for i,c in enumerate(s))
    return [s, s.swapcase()]
    
print(capitalize("abcdef"))