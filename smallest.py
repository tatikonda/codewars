def smallest(n):
    m = n
    s = str(n)
    rg = range(len(s))
    for i in rg:
        for j in rg:
            li = list(s)
            d = li.pop(i)
            li.insert(j, d)
            z = int(''.join(li))
            if z < m:
                m = z
                x = i
                y = j
    return [m, x, y]






print(smallest(261235))