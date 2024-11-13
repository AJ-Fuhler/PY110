"""
Create a function that takes a list of integers as an argument. Determine and
return the index N for which all numbers with an index less than N sum to the
same value as the numbers with an index greater than N. If there is no index
that would make this happen, return -1.

If you are given a list with multiple answers, return the index with the
smallest value.

The sum of the numbers to the left of index 0 is 0. Likewise, the sum of the
numbers to the right of the last element is 0.




P:

input: list of integers
output: integer representing index in input list.

Explicit:
- if there are multiple indexes where the sum of the numbers to the left is 
  equal to the sum of numbers on the right, return the lowest value index.
- return -1 if no index would make that happen.

Implicit:
- 

E:

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)


D:
- list containing all indexes where the situation is truthy.

A:

- given a list of integers
- indexes = []
- for each index from 0 through length of input_list - 1:
  - if sum(input_list[0:index]) == sum(input_list[index + 1:])
    - append to indexes: index

if indexes is not empty:
  - return indexes[0]
else:
  - return -1



"""

def equal_sum_index(numbers):
    indexes = []
    for idx in range(len(numbers)):
        if sum(numbers[0:idx]) == sum(numbers[idx + 1:]):
            indexes.append(idx)
    
    if indexes:
        return indexes[0]
    
    return -1

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)