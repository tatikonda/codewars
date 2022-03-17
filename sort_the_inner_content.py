def sort_the_inner_content(str):
    words = str.split()
    output = []
    
    for word in words:
        if len(word) > 2:
            output.append(word[0] + ''.join(sorted(word[1:-1], reverse=True)) + word[-1])            
        else: output.append(word)
        
    return ' '.join(output)
print(sort_the_inner_content('sort the inner content i descending order'))