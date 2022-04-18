def solve(arr):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nums = range(1,27)
    alpha_dict = dict(zip(alphabet, nums))
    res  = []
    
    for i in arr:
        count = 0
        for n, c in enumerate(i, start=1):
            if n == alpha_dict.get(c.upper()):
                count += 1
        res.append(count)
    return res

print(solve(["IAMDEFANDJKL","thedefgh","xyzDEFghijabc"]))