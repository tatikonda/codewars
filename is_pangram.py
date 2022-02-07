import string

def is_pangram(s):
    return set(s.lower()) >= set(string.ascii_lowercase)


def is_pangram(s):
    s = s.lower()
    for token in string.ascii_lowercase:
        if token not in s:
            return False
    return True            
pangram = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(pangram))