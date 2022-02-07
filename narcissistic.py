from mimetypes import suffix_map


def narcissistic(value):
    sum = 0
    for a in str(value):
        sum += int(a) ** len(str(value))
    return sum == value

print(narcissistic(123))