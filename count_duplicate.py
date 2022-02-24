def duplicate_count(text):
    duplicate_letters = []
    for i in text.lower():
        if text.lower().count(i) > 1 and i not in duplicate_letters:
            duplicate_letters.append(i)
    return len(duplicate_letters)


def duplicate_count1(text):
    lowerText = text.lower()
    found = []
    for char in lowerText:
        if(not(char in found) and lowerText.count(char) > 1):
            found.append(char)
    print(found)
    return len(found)        
print(duplicate_count("MA00URYBSiCQXYcUEV3Tj229ql9ZNkYXI2Kh7SKJvLkR5bF1UtMx7"))
     