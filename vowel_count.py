def get_count(sentence):
    vowels = 'aeiou'
    count_vowels = 0
    for x in sentence:
        if x in vowels:
            count_vowels += 1
    return count_vowels

def get_count(sentence):
    return sum(c in 'aeiou' for c in sentence)

print(get_count('abcdefghijklmn'))