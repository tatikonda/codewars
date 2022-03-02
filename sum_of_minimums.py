def sum_of_minimums(numbers):
    res = 0
    for i in numbers:
        res += sorted(i)[0]
    return res

def sum_of_minimums(numbers):
    return sum(map(min, numbers))
    
print(sum_of_minimums([ [ 7,9,8,6,2 ], [6,3,5,4,3], [5,8,7,4,5] ]))