"""
Create a function that takes a list of integers as an argument and returns the
integer that appears an odd number of times. There will always be exactly one
such integer in the input list.

P:

input: list of integers
output: integer from list that appears an odd number of times

explicit:
- there will always be only one integer that appears an odd number of times

Implicit:
- minimum number of appearances is 1.

E:

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)

D:

use the list itself to iterate over

A:

- for each number in numbers:
  - if the count of number in numbers % 2 != 0:
    - return number





"""

def odd_fellow(numbers):
    for number in numbers:
        if numbers.count(number) % 2 != 0:
            return number
        


print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)