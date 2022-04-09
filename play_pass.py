def play_pass(s, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for i, char in enumerate(s):
        if char.isalpha():
            indx = alphabet.index(char.lower()) 
            new_char = alphabet[(indx+n)%26]
            if i % 2 == 0:
                new_char = new_char.upper()
        elif char.isdigit():
            new_char = str(9-int(char))
        else:
            new_char = char
        output += new_char
    return output[::-1]

print(play_pass("I LOVE YOU!!!", 1))