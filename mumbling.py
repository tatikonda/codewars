def accum(s):
    #https://realpython.com/python-enumerate/
    new = []
    for i, a in enumerate(s):
        new.append(a.upper() + a.lower()*(i))
    return '-'.join(new)

print(accum('abnc'))