#input =  [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]
#output = ["Open", "Open", "Senior", "Open", "Open", "Senior"]
def open_or_senior(data):
    final = []
    for pair in data:
        if pair[0] >= 55 and pair[1] > 7:
            final.append('Senior')
        else:
            final.append('Open')
    return final

print(open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)]))