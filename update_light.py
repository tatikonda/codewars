def update_light(current):
    order = ['green','yellow','red']
    if current == 'green':
        return 'yellow'
    if current == 'yellow':
        return 'red'
    if current == 'red':
        return 'green'

def update_light(current):
    light_order = {'red':'green', 'yellow':'red', 'green':'yellow'}    
    return light_order[current]

print(update_light('green'))