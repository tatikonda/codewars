def proper_fractions(n):
    if n == 1:
        return 0
    euler = n
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            euler *= 1 - 1/p
            while n % p == 0:
                n //= p
    if n > 1:
        euler *= 1 - 1/n
        print(euler)
    return int(euler)

print(proper_fractions(6))