def sum_two_smallest_numbers(numbers):
    n = sorted(numbers)
    return sum(n[:2])

print(sum_two_smallest_numbers([25, 42, 12, 18, 22]))