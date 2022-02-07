def disemvowel(string_):
    return ''.join([l for l in string_ if l not in 'aeiouAEIOU'])

print(disemvowel("This website is for losers LOL!"))