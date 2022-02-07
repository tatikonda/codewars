def spin_words(sentence):
    spin_sentence = []
    for word in sentence.split():
        if len(word) >= 5:
            spin_sentence.append(word[::-1])
        else:
            spin_sentence.append(word)
    return ' '.join(spin_sentence)


def solution(string):
    return string[::-1]

print(spin_words("Rekha what are you doing"))

print(solution("Rekha what are you doing"))