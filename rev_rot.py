def revrot(s, n):
    if not s or n < 1 or n > len(s):
        return ""
    res = ''
    while len(s) >= n:
        group = s[:n]
        if sum([int(d)**3 for d in group]) % 2 == 0:
            res += group[::-1]
        else:
            res += group[1:] + group[0]
        s = s[n:]
    
    return res


print(revrot("12345698765987643894", 6))