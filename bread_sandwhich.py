def slices_to_name(n):
    res = ''
    if n < 2:
        return None
    if n >=2:
        if n % 2 == 0:
            res += 'sandwich '* int(n/2)
        else:
            res += 'bread sandwich sandwich ' + 'sandwich '* int((n - 3)/2)
    return res

def name_to_slices(name):
    if type(name) != str or name == '':
        return None
    name_s = name.split()
    if len(name_s) == 1 and name_s[0] == 'sandwich':
        return 2
    if len(name_s) == 2:
        if name_s[0] == 'bread' and name_s[1] == 'sandwich':
            return 3
        elif name_s[0] == 'sandwich' and name_s[1] == 'sandwich':
            return 4
    if len(name_s) > 2:
        if name_s[0] == 'bread' and name_s[1] == 'sandwich':
            return 3 + (len(name_s)*2 - 3)
        elif name_s[0] == 'sandwich' and name_s[1] == 'sandwich':
            return 4 + (len(name_s)*2 - 4)
    else:
        return None

def slices_to_name(n):
    return (('bread '*(n%2) + 'sandwich '*(n//2)).strip() if isinstance(n, int) and n > 1 else None)

def name_to_slices(name):
    if not (isinstance(name, str) and 'sandwich' in name): return

    if name.find('bread') < 1:
        return name.count('sandwich')*2 + name.count('bread')

print(slices_to_name(3))
print(name_to_slices('bread sandwich'))