def high(x):
    score = 0
    max_sc = 0
    res = ''
    for wrd in x.split():
        score = 0
        # computing score
        for lttr in wrd:
            if lttr in wrd.lower():
                score += ord(lttr) - 96
 
        # updating maximum
        if score > max_sc:
            max_sc = score
            res = wrd
    return res

def high(x):
    highest_score = 0
    for word in x.split(' '):
        score = sum(ord(c)-96 for c in word)
        if score > highest_score:
            highest_score = score
            highest_word = word
            
    return highest_word
    
print(high('hello there'))