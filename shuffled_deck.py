from random import shuffle

def shuffled_deck():
    num_list = list(range(1,14))
    alpha_list = ['H','C','D','S']
    deck = []
    for x in alpha_list:
        for y in num_list:
            deck.append(x+' '+str(y))
    shuffle(deck)
    return deck



def shuffled_deck():
    deck = [f'{x} {i}' for x in "HCDS" for i in range(1, 14)]
    shuffle(deck)
    return deck

print(shuffled_deck())