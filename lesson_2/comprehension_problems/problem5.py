lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def sum_odds(numbers):
    return sum([number for number in numbers 
                      if number % 2 == 1])

print(sorted(lst, key=sum_odds))