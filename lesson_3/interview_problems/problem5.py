"""
Create a function that takes a string argument and returns the
character that occurs most often in the string. 
If there are multiple characters with the same greatest
frequency, return the one that appears first in the string. When counting characters,
consider uppercase and lowercase versions to be the same.




"""

def most_common_char(string):
    letter_dict = {}
    for char in string.casefold():
        letter_dict.setdefault(char, 0)
        letter_dict[char] += 1
    
    most_common = ''
    max_count = 0

    for key, value in letter_dict.items():
        if value > max_count:
            most_common = key
            max_count = value

    return most_common

print(most_common_char('Hello World')  == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')