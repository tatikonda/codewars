def barista(coffees):
    time, total = 0, 0
    for e in sorted(coffees):
        time += e
        total += time
        time += 2
    return total

print(barista([20,5]))