def square_digits(num):
    res = ''
    for l in str(num):
     res += str((int(l))**2)
    return int(res)

def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

print(square_digits(9119))