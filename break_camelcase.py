def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)

def solution(s):
    new=''
    for i in s:
        if i.islower():
            new += i 
        else:
            new += ' '+i
    return new

