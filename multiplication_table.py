def multiplication_table(size):
    
    res = []
    for i in range(1,size+1):
        row = []
        for j in range(1,size+1):
            row.append(j*i)
        res.append(row)
    return res

print(multiplication_table(5))