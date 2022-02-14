def wave(people):
    res = []
    for i in range(len(people)):
        if people[i]!=' ':
            res.append(people[:i]+people[i].upper()+people[i+1:])
    return res

def wave(str):
    return [str[:i] + str[i].upper() + str[i+1:] for i in range(len(str)) if str[i].isalpha()]    
print(wave('hello'))
    