def swap(string_):
    new = ''
    for i in string_:
        if i.islower():
            i = i.upper()
        else:
            i = i.lower()
        new += ''.join(i)
            
    return new

print(swap('HelloWorld'))