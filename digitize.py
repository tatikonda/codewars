def digitize(n):
    new = []
    for i in str(n)[::-1]:
        new.append(int(i))
    return new

def digitize(n):
    return [int(s) for s in str(n)[::-1]]

# Revesre the string and convert to int and return as a list
print(digitize(123))