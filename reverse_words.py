def reverse_words(text):
    new=[]
    for word in text.split(' '):
        new.append(word[::-1])
    return ' '.join(new)

def reverse_words(str):
    return ' '.join(s[::-1] for s in str.split(' '))
print(reverse_words('The quick brown fox jumps over the lazy dog.'))