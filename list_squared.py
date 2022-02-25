def divisors(n):
    divs = [1, n]
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            divs.extend([i, int(n/i)])
    return set(divs)


def list_squared(m, n):
    sq_list = []
    for num in range(m, n):
        _sum = sum(item**2 for item in divisors(num))
        if (_sum ** 0.5).is_integer():
            sq_list.append([num, _sum])
    return sq_list

print(list_squared(42,250))