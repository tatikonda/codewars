def duck_duck_goose(players, goose):
    return players[(goose % len(players)) - 1]

print(duck_duck_goose(['a', 'b', 'c', 'd'], 5))