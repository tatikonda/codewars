def tower_builder(n_floors):
    tower = []
    n = n_floors
    for i in range(n_floors):
        n -= 1
        tower.append(' ' * n + '*' * (i * 2 + 1) + ' ' * n)
    return tower

print(tower_builder(5))