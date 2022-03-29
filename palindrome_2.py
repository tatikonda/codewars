def palindrome(num):
    if type(num) != int or num < 0: return "Not valid"
    s = str(num)
    for i in range(len(s)-2):
        if s[i] == s[i+1] or s[i] == s[i+2]: return True
    return len(s) != 1 and s[-1] == s[-2]

print(palindrome(1221))