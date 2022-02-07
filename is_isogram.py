def is_isogram(string):
    for i in string.lower():
        if string.lower().count(i) > 1:
            return False
    return True

# If count is greater than 1, return False

print(is_isogram(""))

