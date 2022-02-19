
def find_difference(a, b):
    return abs((a[1]*a[2]*a[0])-b[1]*b[2]*b[0])

print(find_difference([3, 2, 5], [1, 4, 4]))