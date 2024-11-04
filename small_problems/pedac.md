Write a function that takes a string as an argument and returns that string
with every occurrence of a "number word" -- 'zero', 'one', 'two', 'three',
'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted to its
corresponding digit character.

You may assume that the string does not contain any punctuation.

1. Understanding the Problem

input: string
output: string with all "number words" converted to digits.

requirements:
  
  Explicit:
  - within a given string, convert each occurence of a "number word' to its
    corresponding digit. etc. 'one' needs to be converted to '1'.
  - string won't contain any punctuation.

  Implicit:
  - 

2. Examples and Test Cases

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

3. Data Structures

- list to separate all words
- dictionary containing "number words" as keys, digits as values from 0-9

4. algorithm

- given a string
- create an empty string
- split all words into a list of strings
- create dictionary with number words as keys, digits as values
- for each word in list_strings
  - if word in dictionary:
    - empty_string = empty_string + dictionary[word]
    else:
    - empty_string += word
- return empty_string