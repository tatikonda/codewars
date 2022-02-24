def duplicate_count(text):
    duplicate_letters = []
    for i in text.lower():
        if text.lower().count(i) > 1 and i not in duplicate_letters:
            duplicate_letters.append(i)
    return len(duplicate_letters)


def duplicate_count(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])
      
print(duplicate_count("MA00URYBSiCQXYcUEV3Tj229ql9ZNkYXI2Kh7SKJvLkR5bF1UtMx7"))
     