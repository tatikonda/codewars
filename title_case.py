def title_case(title, minor_words=''):
    minor_words = [word.lower() for word in minor_words.split(' ')]
    title_case = []
    for i, word in enumerate(title.split()):
        
        if i == 0:
            title_case.append(word.title())
            continue
        if word.lower() in minor_words:
            title_case.append(word.lower())
            continue
        title_case.append(word.title())
    
    return ' '.join(title_case)

print(title_case('THE WIND IN THE WILLOWS', 'The In'))