def high_and_low(numbers):
    n = [int(i) for i in numbers.split()]
    return " ".join([str(max(n)), str(min(n))])

print(high_and_low("1 2 13 36 -5"))