import datetime

def friday_the_13ths(year):
    thirteens = [datetime.date(year, month, 13)
                 for month in range(1, 13)]
    
    
    count = 0
    for day in thirteens:
        if day.weekday() == 4:
            count += 1

    return count


print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True