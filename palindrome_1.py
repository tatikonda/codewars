def palindrome(num,s):
    if not (type(num) == type(s) == int) or num < 0 or s < 0:
        return 'Not valid'
    
    res = []
    num = max(num, 11)
    while len(res) != s:
        if str(num) == str(num)[::-1]:
            res.append(num)
        num += 1
    return res

print(palindrome(6,4))