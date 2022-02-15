def number(lines):
    count = 1
    line = []
    for x in lines:
        line.append(str(count) + ': ' + x)
        count += 1
    return line

def number(lines):
    return [f"{counter}: {line}" for counter, line in enumerate(lines, start=1)]
print(number(["a", "b", "c"]))