def add_length(str_):
    res = []
    for word in str_.split():
        res.append(word+' '+str(len(word)))
    return res

def add_length(str_):
    return [f"{word} {len(word)}" for word in str_.split()]

print(add_length('apple ban'))