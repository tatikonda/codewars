def is_square(n):
    if n < 0:
        return False
    if n >= 0:
        if (n ** 0.5) % 1 == 0:
            return True
        else:
            return False

def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0

print(is_square(9))