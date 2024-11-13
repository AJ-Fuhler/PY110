"""
Create a function that takes a string as an argument and returns True if the
string is a pangram, False if it is not.

Pangrams are sentences that contain every letter of the alphabet at least once.
For example, the sentence "Five quacking zephyrs jolt my wax bed." is a pangram
since it uses every letter at least once. Note that case is irrelevant.

P:

input: string
output: True or False representing whether the string is a pangram or not.

Explicit:
- case is irrelevant
- a pangram is a sentence than contains every letter of the alphabet at least
  once

Implicit:
- 

E:

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)

D:
- dictionary for all letters in alphabet as keys, False as starting value.

A:
- use dictionary comprehension to create the dict.
- given a string
- create dictionary with all characters in the alphabet as keys, False as 
  start value.
- for each character in the lowercase string:
  - if character is alphabetic:
    - dictionary[character] = True

- return True if all values in dictionary are True, False otherwise

"""

def is_pangram(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alpha_dict = {char: False for char in alphabet}
    for char in string.lower():
        if char.isalpha():
            alpha_dict[char] = True
    
    return all(value for value in alpha_dict.values())


print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)