def number(bus_stops):
    people_in = 0
    people_out = 0
    for i in bus_stops:
        people_in += i[0]
        print(people_in)
        people_out += i[1]
        print(people_out)
    return people_in - people_out


print(number([[10,0],[3,5],[5,8]]))