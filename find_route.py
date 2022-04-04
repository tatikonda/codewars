def find_routes(routes):
    routes = dict(routes)
    places = list(routes.keys() - routes.values()) # Get the starting element for route
    try:
        for place in places:
            places.append(routes[place])
    finally:
        return ', '.join(places)

print(find_routes([('ITA','GER'), ('GER','BEL'), ('BEL','CAN'), ('ABC', "ITA")]))   

