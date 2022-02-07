def tribonacci(signature, n):
    if n <= 2:
        return signature[:n]
    res = 0
    for i in range(n - len(signature)):
        res = sum(signature[-3:])
        signature.append(res)
    return signature

def tribonacci(signature, n):
  res = signature[:n]
  for i in range(n - 3): res.append(sum(res[-3:]))
  return res

print(tribonacci([1, 1, 1], 1))