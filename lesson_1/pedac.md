"""
PROBLEM:

Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection
should be case-sensitive.
"""

1. Understanding the Problem

input: string
output: list containing all palindromic substrings that are 2 or more characters.

requirements:
  
  explicit:
  - palindromes need to be 2 or more characters long
  - palindrome detection should be case-sensitive (MOM is a palindrome, Mom is not)
  - return only substrings that are palindromes.
  
  implicit:
  - output needs to be a list
  - if no palindromes are found, return empty list
  - when given an empty string, return empty list

2. examples and test cases

# Comments show expected return values
palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
palindrome_substrings("palindrome") # []
palindrome_substrings("")           # []
palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]

3. Data structure

- list

4. algorithm

- declare a result variable and initialize it to an empty list
- create a list named substr_list that contains all the substrings of the input   string that are at least 2 characters long.
- loop through the words in the substr_list.
- If the word is a palindrome, append it to the result list.
- return The result list.

substrings function:

- if given the string 'halo', it should return all possible substrings of 2 or more characters.
- h: ha, hal, halo
- a: al, alo
- l: lo
- o: can't produce substring of 2 or more characters.

This means our outerloop will loop from index 0 through next to last index. Our
innerloop will need to loop from substrings of length 2 through substrings of maximum substrings length, which will be length of string - current index?

- create an empty list to hold the resulting substrings
- for each start_index from 0 through the next to last index position
  - for each length value from 2 through length of string - start_index:
    - extract the substring of that length starting at the current index
      position.
    - add the substring to our resulting list

- return the resulting list