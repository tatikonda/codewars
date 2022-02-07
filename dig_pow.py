def dig_pow(n, p):
    sum = 0
    for y, x in enumerate(str(n)):
        sum += int(x) ** (p+y)
    return int(sum/n) if sum % n == 0 else -1

# Enumerate, sum the numbers to the power and get the total
# if mod is 0, return the number, else return -1

print(dig_pow(46288,3))