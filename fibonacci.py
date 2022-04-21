def fibonacci(n: int) -> int:
    x, y = 0, 1
    for i in range(n):
        x, y = y, y + x
    return x

print(fibonacci(34))