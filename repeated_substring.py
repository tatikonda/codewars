def f(s):
    for i in range(1, len(s) + 1):
        print(s[:i])
        t, k = s[:i], int(len(s) / i)
        if t * k == s:
            return (t, k)

print(f("efefef"))