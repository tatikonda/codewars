def presses(phrase):
    taps = {
            1 : '1ADGJMPTW *#',
            2 : 'BEHKNQUX0',
            3 : 'CFILORVY',
            4 : '23456S8Z',
            5 : '79'
            }
    output = 0
    for letter in (phrase):
        for key, value in taps.items():
            if letter.upper() in value:
                output += key
    return output

print(presses("HOW R U"))