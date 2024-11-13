"""
Create a function that takes a single integer argument and returns the sum of
all the multiples of 7 or 11 that are less than the argument. If a number is a
multiple of both 7 and 11, count it just once.

For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and
22. The sum of these multiples is 75.

If the argument is negative, return 0.

P:

input: integer
output: integer representing sum of all unique multiples of 7 and 11 that are
less than the input integer.

Explicit:
- if the argument is negative, return 0
- if a number is a multiple of both 7 and 11, count it just once.
- return the sum of all mulitples of 7 and 11 that are less than the argument.

implicit:
- if argument is 0, return 0.

E:

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)

D:
- set collecting all unique multiples of 7 and/or eleven.

A:
- given an input_integer
- if input_integer <= 0:
  - return 0

- create an empty set
- for each number from 1 through input_integer - 1:
  - if number % 7 == 0 or number % 11 == 0:
    - add number to set

- return the sum of set




"""

def seven_eleven(number):
    multiples_of_7_11 = {num for num in range(1, number)
                         if num % 7 == 0 or num % 11 == 0}
    return sum(multiples_of_7_11)

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)