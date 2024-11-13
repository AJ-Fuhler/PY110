"""
Create a function that takes a non-empty string as an argument. 
The string consists entirely of lowercase alphabetic characters. 
The function should return the length of the longest vowel substring. 
The vowels of interest are "a", "e", "i", "o", and "u".

P:

input: string
output: integer representing length of the longest vowel substring

explicit:
- the vowels of interest are 'aeiou'
- return an integer

implicit:
- can have 0 vowels
- if one vowel, return 1

E:

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)

D:
- string of all vowels
- integer to keep track of highest number of vowels in a row

A:

- given a string
- vowels = 'aeiou'
- vowels_in_row = 0
- row_list = []
- index = 0
- while index < length of string:
  - if string[index] in vowels:
    - vowels_in_row += 1
  - else:
    - row_list.append(vowels_in_row)
    - vowels_in_row = 0

- return max(row_list)


"""

def longest_vowel_substring(string):
    vowels = 'aeiou'
    vowels_in_row = 0
    row_list = []
    index = 0
    while index < len(string):
        if string[index] in vowels:
            vowels_in_row += 1
        else:
            row_list.append(vowels_in_row)
            vowels_in_row = 0
        index += 1
    
    
    row_list.append(vowels_in_row)

    return max(row_list)

def longest_vowel_substring(string):
    vowels = 'aeiou'
    current_length = 0
    max_length = 0

    for char in string:
        if char in vowels:
            current_length += 1
            max_length = max(current_length, max_length)
        else:
            current_length = 0
    
    return max_length

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)