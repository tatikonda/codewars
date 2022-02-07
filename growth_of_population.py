def nb_year(p0, percent, aug, p):
    #1000 + 1000 * 0.02 + 50
    no_of_year = 1
    total_population_year = (p0 + int(p0 * (percent/100)) + aug)
    while p > total_population_year:
        no_of_year+=1
        p0 = total_population_year
        total_population_year = (p0 + int(p0 * (percent/100)) + aug)
    return no_of_year

print(nb_year(1500, 5, 100, 5000))
