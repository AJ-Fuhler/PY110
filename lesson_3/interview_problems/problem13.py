"""
Create a function that takes two strings as arguments and returns True if some
portion of the characters in the first string can be rearranged to match the
characters in the second. Otherwise, the function should return False.

You may assume that both string arguments only contain lowercase alphabetic
characters. Neither string will be empty.

P:

input: string1, string2
output: True or False, depending on whether the characters in string1 can make
up string2 if rearranged.

Explicit:
- both strings only contain lowercase alphabetic characters
- neither string will be empty

Implicit:
- 

E:

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)

D:
Dictionary consisting of all characters in string2 as keys, False values

A:
- given 2 strings
- create dictionary with every character of string2 as keys, False as values
- for each char in string1:
   - if char in string2:
     - dictionary[char] = True

- return True if all values in dictionary are True, False otherwise

"""

def unscramble(string1, string2):
    char_dict = {char: 0 for char in string2}
    for char in string1:
        if char in string2:
            char_dict[char] += 1
    
    return all([value == string2.count(key) for key, value in char_dict.items()])

print(unscramble('ansucchlhloo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)