def unused_digits(*args):
    digits='0123456789'
    return "".join(n for n in digits if n not in str(args))


print(unused_digits(12, 34, 56, 78))