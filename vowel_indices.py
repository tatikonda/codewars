def vowel_indices(word):
    vowels='aeiouy'
    res=[]
    for n,c in enumerate(word, start=1):
        if c.lower() in vowels:
            res.append(n)
    return res



print(vowel_indices("apple"))