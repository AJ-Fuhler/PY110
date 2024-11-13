"""
Create a function that takes a nonempty string as an argument and returns a
tuple consisting of a string and an integer. If we call the string argument s,
the string component of the returned tuple t, and the integer component of the
tuple k, then s, t, and k must be related to each other such that s == t * k.
The values of t and k should be the shortest possible substring and the largest
possible repeat count that satisfies this equation.

You may assume that the string argument consists entirely of lowercase
alphabetic letters.

P:

input: string
output: tuple containing string and integer

explicit:
- string, (substring and integer) must be related like this:
   string == (substring * integer)
- string argument will be all lowercase alphabetic characters

Implicit:
- 

E:

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))

D:
- loop to go through all possible substrings from index 0 as a start.

A:

- given a string
- for each index in a range from 1 through length of string - 1:
  - if string from 0 through index * (length of string // index) == string:
    - return in a tuple: string[0:index], length of string // index



"""

def repeated_substring(string):
    for idx in range(1, len(string) + 1):
        if string[0:idx] * (len(string) // idx) == string:
            return (string[0:idx], len(string) // idx)


print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))