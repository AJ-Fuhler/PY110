Write a function that takes a string of digits and returns the appropriate
number as an integer. You may not use any of the standard conversion functions
available in Python, such as int. Your function should calculate the result by
using the characters in the string.

For now, do not worry about leading + or - signs, nor should you worry about
invalid characters; assume all characters are numeric.

1. Understanding the Problem

Input: string containing digits
Output: integer corresponding to digits in input string

Requirements:

  Explicit:
  
  - may not use any standard conversion functions available, like int.
  - result should be calculated using the characters in the string.
  - all characters in string will be numeric.

  Implicit:
  - 


Questions:

- Can string be empty? NO?

2. Examples and Test Cases

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True


3. Data Structures

integer: result must be an integer

4. Algorithm

- given 'num_string'
- 'result' = 0
- 'multiplier' = 1
- str_num_dict = dictionary containing all digits as strings as keys, and
  the corresponding integer as its associated value
- for each 'num' in reversed 'num_string':
    - int_num = str_num_dict['num']
    - result = result + int_num * multiplier
    - multiplier = multiplier * 10

return result