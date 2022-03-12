def battle(x,y):
    NUM = 26
    num_list = list(range(1,NUM+1))
    alpha_list = [chr(c) for c in list(range(ord('A'),ord('Z')+1))]
    my_dict = dict(zip(alpha_list, num_list))
    sum_x, sum_y = 0,0
    for c in x:
        if c.islower():
            sum_x += my_dict.get(c.upper())/2
        else:
            sum_x += my_dict.get(c)
    sum_x = sum_x
    for c in y:
        if c.islower():
            sum_y += my_dict.get(c.upper())/2
        else:
            sum_y += my_dict.get(c)
    sum_y = sum_y
    if sum_x == sum_y:
        return 'Tie!'
    elif sum_x > sum_y:
        return x
    else:
        return y    


def battle(x: str, y: str) -> str:
    first = sum(ord(char)%64 if char.isupper() else .5*(ord(char)%96) for char in x)
    second = sum(ord(char)%64 if char.isupper() else .5*(ord(char)%96) for char in y)
    
    return x if first > second else y if first < second else "Tie!"
    
print(battle('Hi', 'AB'))