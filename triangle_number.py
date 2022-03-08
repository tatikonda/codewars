def sum_triangular_numbers(n):
    sum_= 0
    temp_ = 0
    for i in range(1,n+1):
        temp_ += i
        sum_ += temp_
        
    return sum_

print(sum_triangular_numbers(4))