
from calendar import weekday, day_name

def most_frequent_days(year):
    print(sorted( {weekday(year, 1, 1), weekday(year, 12, 31)} ))
    for day in sorted( {weekday(year, 1, 1), weekday(year, 12, 31)} ):
        return [ day_name[day]  ]



print(most_frequent_days(2023))