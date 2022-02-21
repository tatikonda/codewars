def order(sentence):
    if sentence == '':
        return ''
    res = []
    for i in range(1,len(sentence.split())+1):
        for word in sentence.split():            
            if str(i) in word:
                res.append(word)
    return ' '.join(res)

print(order("is2 Thi1s T4est 3a"))