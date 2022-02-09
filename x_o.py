def xo(s):
    count_o = 0
    count_x = 0
    for i in s:
        if i.lower() == 'x':
            count_x += 1
        if i.lower() == 'o':
            count_o += 1
    return True if count_o == count_x else False


def xo(s):
    s = s.lower()
    return s.count('x') == s.count('o')
    
print(xo("xxooo"))
