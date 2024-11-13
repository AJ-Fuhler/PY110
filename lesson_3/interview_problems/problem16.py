"""
Create a function that returns the count of distinct case-insensitive
alphabetic characters and numeric digits that occur more than once in the input
string. You may assume that the input string contains only alphanumeric
characters.

P:

input: string
output: count of case-insesitive alphanumeric characters that occur more than
once in the input string.

Explicit:
- string contains only alphanumeric characters
- compare case-insensitive
- return a integer

implicit:
- when no character occurs more than once, return 0

E:

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

D:

- dictionary to contain all characters as keys, counts of characters as values.
- count variable to capture amount of characters than occur more than once.

A:

- given a string
- create an empty dictionary
- for each char in string:
  - if dict[char] already in string:
    - dict[char] += 1
  - else:
    - dict[char] = 1

- count = 0
- for each value in dict:
  - if value >= 2:
    - count += 1

return count





"""

def distinct_multiples(string):
    char_dict = {}
    for char in string.casefold():
        char_dict.setdefault(char, 0)
        char_dict[char] += 1
    
    count = 0
    for value in char_dict.values():
        if value >= 2:
            count += 1
    
    return count

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5