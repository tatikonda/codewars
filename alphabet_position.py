def alphabet_position(text):
    new=''
    for c in text.lower():
        if c.isalpha():
            new += (str(ord(c)- 96)) + ' '
    return new

def alphabet_position(text):
    return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

def high(x):
    total_for_each_word = 0
    max = 0
    result = ''
    for word in x.split():
        total_for_each_word = 0
        print(word)
        for i in word.lower():
            total_for_each_word += ord(i) - 96
            print(total_for_each_word)
            if total_for_each_word > max:
                max = total_for_each_word
                result = word
        return result

# ord() returns an integer representing the Unicode character
# ord(a) is 97, so we subtract 96 to get the position to 1
# isalpha() checks if character is an alphabet (a-z)
print(alphabet_position('hello'))
print(high('hello there'))
