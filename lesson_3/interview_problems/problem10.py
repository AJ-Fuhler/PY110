"""
Create a function that takes a string of digits as an argument and returns the number of even-numbered substrings
that can be formed. 
For example, in the case of '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', 
for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a separate substring.

P:

input: string of digits
output: integer representing number of even-numbers substrings that can be formed

explicit:
- if substring occurs more than once, count them as separate substrings.

implicit:
- if no even numbers, return 0


E:

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

D:

- list of all possible substrings
- list of even-numbers substrings

A:

- given a string of digits:
- substrings = []
- for each index from range of 0 to but not including length of string:
  - for each jdex from range of index + 1 through but not including length of string:
    - append to substring string[index:jdex]





"""

def even_substrings(digits):
    substrings = []
    for idx in range(len(digits)):
        for jdx in range(idx + 1, len(digits) + 1):
            substrings.append(digits[idx:jdx])
    
    even_substring_list = [digit for digit in substrings if int(digit) % 2 == 0]
    
    return len(even_substring_list)

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)