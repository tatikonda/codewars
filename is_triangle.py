def is_triangle(a, b, c):
    if int(a + b) > int(c) and int(b + c) > int(a) and int(a + c) > int(b):
        return True

def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c
    
print(is_triangle(1, 2, 2))