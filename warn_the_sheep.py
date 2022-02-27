def warn_the_sheep(queue):
    queue = queue[::-1]
    wolf_counter = None
    for i, animal in enumerate(queue):
        if animal == 'wolf':
            wolf_counter = i
    if wolf_counter == 0:
        return 'Pls go away and stop eating my sheep'
    return f'Oi! Sheep number {wolf_counter}! You are about to be eaten by a wolf!'
        

def warn_the_sheep(queue):
    i = queue[::-1].index('wolf')
    if i == 0:
        return 'Pls go away and stop eating my sheep'
    return f'Oi! Sheep number {i}! You are about to be eaten by a wolf!'
    
print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']))