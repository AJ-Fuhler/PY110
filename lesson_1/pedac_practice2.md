Sort Strings by Most Adjecent Consonants:

Given a list of strings, return a new list where the strings are sorted based on the highest number of adjacent consonants a string contains. If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other. Consonants are considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.

1. Understanding the Problem:

Input: list of strings

Output: A new sorted list of strings based on highest number of adjacent consonants
        a string contains.


Requirements:
  Explicit:
    - List needs to be ordered based on highest number of adjacent consonants
       contained in a string.
    - If two strings contain the same highest number of adjacent consonants,
       they should retain their original order in relation to each other.
    - Consonants are considered adjacent if they are next to each other in the
       same word or if there is a space between two consonants in adjacent words.
    - A new list object needs to be returned.

  Implicit:
    - Strings may contain single or multiple words
    - Strings may not be empty.
    - Strings may have no adjacent consonants
    - Strings should be sorted in descending order
    - Case is not relevant.
    - Single consonants in a string do not affect sort order in comparison to
      strings with no consonants. Only adjacent consonants affect sort order. 

Questions:

  - does that mean that 'abc cdf' has 5 adjacent consonants? / What is meant by
     'a space between two consonants in adjacent words'? YES
  - Do strings always contain multiple words? NO
  - Can strings be empty? NO?
  - Is it possible for a string to contain no adjacent consonants? YES
  - Should the strings be sorted in ascending or descending order? DESCENDING
  - Is case important? NO?


2. Examples and test cases:

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']


3. Data structures

We will be building a new list object.

Something to track the number of adjacent consonants per string could be kept
in a dictionary perhaps:

{
    'aa': 0,
    'baa': 0,
    'ccaa': 2,
    'dddaa': 3,
    'rstafgdjecc': 4,
}

4. Algorithm

High-Level algorithm:

1. for each string:
  - find out the highest number of adjacent consonants within that string.
2.  Sort the input list based on the calculated highest number consonants from
step 1.
3. return sorted list.


sub-algorithm for step 1:

Given a string, return a count of the highest number of adjacent consonants
in that string.

Input: String
Output: An integer representing a count of the highest number of adjacent
        consonants in the string.

print(count_max_adjacent_consonants('dddaa'))       # 3
print(count_max_adjacent_consonants('ccaa'))        # 2
print(count_max_adjacent_consonants('baa'))         # 0
print(count_max_adjacent_consonants('aa'))          # 0
print(count_max_adjacent_consonants('rstafgdjecc')) # 4

- we need to manipulate the input string to remove any spaces.
- we don't want to update the count if the temporary string only contains one
  consonant.

Algorithm:

- Remove the spaces from the 'input string'.
- Initialize a 'maximum consonants count' to zero.
- Initialize an 'adjacent consonants string' to an empty string.
- For each 'letter' in the 'input string':
    - If the 'letter' is a consonant:
        - Concatenate it to the 'adjacent consonants string'.
    - If the letter is a vowel:
        - If the 'adjacent consonants string' has a length
           greater than the current 'maximum consonants count':
             - If the 'adjacent consonants string' has a length
               greater than 1:
                  - Set the 'maximum consonants count' to the length of
                    the 'adjacent consonants string'.
        
        - Reset the 'adjacent consonants string' to an empty string

- Return the 'maximum consonants count'.
    