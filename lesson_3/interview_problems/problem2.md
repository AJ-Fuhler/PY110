Create a function that takes a list of integers as an argument. The function
should return the minimum sum of 5 consecutive numbers in the list. If the list
contains fewer than 5 elements, the function should return None.

P:

input: list of integers
output: integer representing smallest sum of 5 consecutive numbers in the list.

explicit:
- If the list contains less than 5 elements, return None



E:

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

D:

- integer to keep track of smallest sum
- loop

A:

- if length of number < 5:
  - return None
- initialize smallest_sum to the first 5 elements in list_numbers
- for each index from 1 - length of list_numbers - 5:
  - if sum(list_numbers[index:index+5]) < smallest_sum:
    - smallest_num = sum(list_numbers[index:index + 5])

return smallest_sum