def pattern(n):
    res = []
    for i in range(0,n):
        j = i+1
        if j > 1:
            res.append('1'+'*'*i+str(j))
        else:
            res.append(str(j))
    return '\n'.join(res)
    
print(pattern(5))