"""
Create a function that takes a list of integers as an argument and returns a
tuple of two numbers that are closest together in value. If there are multiple
pairs that are equally close, return the pair that occurs first in the list.

input: list of integers
output: tuple containing two numbers that are closest together in value

explicit:
- if there are multiple pairs that are equally close, return the pair that 
  occurs first in the list

E:

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))

D:
- list containing all possible value combinations in tuples
- sorting function returning the difference in value for each tuple

A:
- given a list of numbers
- tuples_list = []
- for each index from 0 through the length of numbers - 2:
  - for each jdex from (index + 1) through length of numbers - 1:
    - append to tuples_list: (numbers[idx], numbers[jdex])

- sort tuples_list using custom_sort as key argument
- return tuples_list[0]

custom_sort(tup):
- return max(tup) - min(tup)

"""

def closest_numbers(numbers):
    tuples_list = []
    for idx in range(len(numbers) - 1):
        for jdx in range(idx + 1, len(numbers)):
            tuples_list.append((numbers[idx], numbers[jdx]))
    
    tuples_list.sort(key=custom_sort)

    return tuples_list[0]

def custom_sort(tup):
    return max(tup) - min(tup)

print(closest_numbers([5, 25, 15, 11, 20])  == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))
