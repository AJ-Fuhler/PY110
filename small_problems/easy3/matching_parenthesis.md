Write a function that takes a string as an argument and returns True if all
parentheses in the string are properly balanced, False otherwise. To be
properly balanced, parentheses must occur in matching '(' and ')' pairs.

input: string
output: Boolean (True or False)

1. Understanding the Problem

Check the string for if it contains parentheses, if it does, make sure all
parentheses are balanced. This means for every '(', there needs to be a ')'.

Requirements:

  Explicit:
  - return True if all parentheses are balanced, False otherwise
  - balanced pairs must start with a '('

  Implicit:
  - If no parentheses present, return True


2. Examples and Test Cases

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

3. Data Structures

- Can we derive all information from just the string?
- use a list, to look up and delete parenthesis pairs after confirming?

4. Algorithm

- given a string
- if '(' is in the string but not ')':
    - return False
- list_of_chars = string converted to list of individual characters
- if ')' appears at an earlier index than '(':
    - return False
- while the count of '(' in string is not 0:
    - find the index of the first '('
    - find the index of the first ')'
    - if index of the '(' is less than index of ')':
        - Remove both elements from list
    - else:
        - Return False
- return True if no more parentheses remain
        



