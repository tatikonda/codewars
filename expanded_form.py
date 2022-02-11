def expanded_form(num):
    res = []
    for index,digit in enumerate(str(num)):
        if digit != '0':
            res.append(digit+'0'*(len(str(num)[index:])-1))
    return ' + '.join(res)

print(expanded_form(70304))
