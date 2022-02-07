def century(year):
    return int(year / 100) + (year % 100 > 0)

print(century(101))