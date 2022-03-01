def evaporator(content, evap_per_day, threshold):
    days = 0
    limit = threshold/100*content
    while content >= limit:
        content -= evap_per_day/100*content
        days += 1
    return days

print(evaporator(10, 10, 10))