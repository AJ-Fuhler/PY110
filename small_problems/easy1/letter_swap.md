Given a string of words separated by spaces, write a function that swaps the
first and last letters of every word.

You may assume that every word contains at least one letter, and that the
string will always contain at least one word. You may also assume that each
string contains nothing but words and spaces, and that there are no leading,
trailing, or repeated spaces.

1. Understanding the Problem

Input: string
Output: string with every first and last letter of each word swapped.

Requirements:
  
  Explicit: 

  - Return a new string, with every first and last letter swapped for
    each word.
  - Every word contains at least one letter.
  - Every string contains at least one word.
  - string will contain nothing but words and spaces, with no leading, 
    trailing or repeated spaces.

  Implicit:
  
  - The smallest string than can be encountered will be a one character string
  - Leave case as is. 

Questions:

- What to do when encountering a one character string? return as is? YES


2. Examples and Test Cases

print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
    

3. Data Structures

list: to separate words and perform necessary operations on them
string: required object to return

4. Algorithm

- given a 'string'
- create a 'words' variable as an empty list
- split all words in 'string' and add them as elements to 'words'
- for each 'word' in 'words':
    - set 'word' to a list of individual character from that word
    - variable 'first_char' = character at index 0
    - remove character at index 0
    - variable 'last_char' = character at last index
    - remove character at last index
    - append 'first_char' to 'word'
    - insert 'last_char' to 'word' at index 0
    - join the word back into a string
    - reassign the element at the current index to 'word'

- join the words back into a string
- return the string