def points(games):
    total = 0
    for j in games:
        i = j.split(':')
        if i[0] > i[1]:
            total += 3
        if i[0] == i[1]:
            total += 1

    return total            


print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))