def race(v1, v2, g):
    if v1 >= v2:
        return None
    else:
        time = g / (v2 - v1)
        h = int(time)
        mn = int((time * 60) % 60)
        s = int((time*3600) % 60)
        time_required = [h, mn, s]
    return time_required

def race(v1, v2, g):
    t = 3600 * g/(v2-v1)
    return [t/3600, t/60%60, t%60] if v2 > v1 else None

print(race(720, 850, 70))