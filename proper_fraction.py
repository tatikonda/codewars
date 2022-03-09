def proper_fractions(n):
    if n==1: return 0
    phi = n
    for p in range(2, int(n**.5)+1):
        if n%p==0: # these p's will always be primes
            phi -= phi/p
            while n%p==0: # take out all the powers of this prime
                n /= p
    if n>1: # if n itself is a prime
        phi -= phi/n
    return int(phi)

print(proper_fractions(6))