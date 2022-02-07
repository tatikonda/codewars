def find_it_(seq):
    res = 0      
    # Traverse the array
    for element in seq:
        print(element)
        # XOR with the result
        res = res ^ element
        print("---", res)
    return res

def find_it(seq):
    for i in seq:
        print(i)
        if seq.count(i)%2!=0:
            print(seq.count(i))
            return i
# Test array
arr = [ 3, 2, 1, 4, 1, 2, 4, 3, 1, 2, 4, 4, 1, 2, 2 ]
print (find_it(arr))