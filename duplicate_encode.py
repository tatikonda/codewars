def duplicate_encode(word):
    new=[]
    for i in word.lower():
        if word.lower().count(i) == 1:
            new.append('(')
        else:
            new.append(')')

    return ''.join(new)


print(duplicate_encode("recesses"))