def direction(facing, turn):
    dir = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    turns = turn//45
    start_idx = dir.index(facing)
    end_idx = (turns+start_idx) % 8
    return dir[end_idx]

print(direction('SE', -45))