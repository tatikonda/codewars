import math

def find_next_square(sq):
    root = math.sqrt(sq)
    print(root)
    if sq == int(root) ** 2:
        return int(root+1) ** 2
    else:
        return -1
        

def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1
    
print(find_next_square(121))
