def encrypt_this(text):
    words = text.split()
    for k, w in enumerate(words):
        if len(w) > 2 :
            words[k] = str(ord(w[0])) + w[-1] + w[2:-1] + w[1]
        else:
            words[k] = str(ord(w[0])) + w[1:]
    return " ".join(words)

print(encrypt_this('A wise old owl lived in an oak'))