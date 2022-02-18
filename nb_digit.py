def nb_dig(n, d):
    count = 0
    for i in range(n+1):
        sq = i*i
        for i in str(sq):
            if i == str(d):
                count += 1
    return count

print(nb_dig(5750,0))


