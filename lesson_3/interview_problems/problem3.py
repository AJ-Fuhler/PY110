"""
Create a function that takes a string argument and returns a copy of the string
with every second character in every third word converted to uppercase. Other
characters should remain the same.

P:

input: string output: new string with every second character in every third
word converted to uppercase.

Explicit:
- Every third word of a string, for that word, every second character needs to
  be converted to uppercase
- Other characters should remain the same.

Implicit:
- If a third word is a one character word, it needs to remain the same.

E:

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)

D:
- list of words, use indexing to select every third.

A:

- given a string
- split_string = list of words
- if length of split_string >= 3:
  - for every idx from 2 through length of string, with steps of 3:
    - convert(split_string, idx)

- join split_string back together into a 'result' string
- return result

convert:
- given a list and an idx
- new_string = ''
- if the length of list[idx] > 1:
  - for every char_idx in range from 0 - len(list[idx]):
    - if char_idx != 0 and char_idx % 2 != 1:
      - new_string += list[idx][char_idx].upper()
    else:
      - new_string += list[idx][char_idx]

list[idx] = new_string

"""

def to_weird_case(string):
    split_string = string.split()
    if len(split_string) >= 3:
        for idx in range(2, len(split_string), 3):
            convert(split_string, idx)
    
    return ' '.join(split_string)

def convert(words, idx):
    new_string = ''
    if len(words[idx]) > 1:
        for char_idx in range(len(words[idx])):
            if char_idx != 0 and char_idx % 2 == 1:
                new_string += words[idx][char_idx].upper()
            else:
                new_string += words[idx][char_idx]
        
        words[idx] = new_string


original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)