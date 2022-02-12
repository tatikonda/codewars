def unique_in_order1(iterable):
    is_in = ''
    res = []
    for char in iterable:
        if char != is_in:
            is_in = char
            res.append(char)
    return res

def unique_in_order(iterable):
    r = []
    for x in iterable:
        x in r[-1:] or r.append(x)
    return r

print(unique_in_order('AAAABBBCCDAABBB'))
