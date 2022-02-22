def increment_string(strng):
    num = ''
    strn = ''
    head = strng.rstrip('0123456789')
    tail = strng[len(head):]
    for l in strng:
        if l.isdigit():
            num += l
        else:
            strn += l
    return strn+str(int(num)+1).zfill(len(tail))

print(increment_string("foobar0043"))