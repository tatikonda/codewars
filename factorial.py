def factorial(n):
    f = 1
    if n == 0:
        return f
    elif n < 0 or n > 12:
        raise ValueError("value out of range")
    else:
        for i in range(1,n+1):
            f *= i
    return f

print(factorial(13))
