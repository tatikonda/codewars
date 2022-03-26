def sentencify(words):
    res = ' '.join(words) + '.'
    return res[0].upper() + res[1:]

print(sentencify(["i", "am", "an", "AI"]))