def human_years_cat_years_dog_years(human_years):
    result = []
    i = human_years
    if i == 1:
        result.append(i)
        result.append(15)
        result.append(15)
    if i == 2:
        result.append(i)
        result.append(15+9)
        result.append(15+9)
    if i >=3:
        result.append(i)
        result.append(15+9+(i-2)*4)
        result.append(15+9+(i-2)*5)       


    return result

def human_years_cat_years_dog_years(x):
    return [x, 24+(x-2)*4 if (x != 1) else 15, 24+(x-2)*5 if (x != 1) else 15]
    
print(human_years_cat_years_dog_years(10))