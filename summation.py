def summation(num):
    sum = 0
    for i in range(num+1):
        sum += i
    return sum

def summation(num):
    return sum(range(1,num+1))
    
print(summation(1))
