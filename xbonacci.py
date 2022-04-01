def Xbonacci(signature,n):
    res = signature[:n]
    for i in range(n - len(signature)): res.append(sum(res[-len(signature):]))
    return res

print(Xbonacci([1,0,0,0,0,0,0,0,0,0],20))