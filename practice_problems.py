target_letters = ['a', 'b', 'c', 'd', 'e']
characters = ['a', 'b', 'b', 'd', 'f', 'f', 'z', 'z', 'z']

result = {key: {'present': key in characters, 'count': characters.count(key)} 
          for key in target_letters}

print(result)

# {
#     'a': { 'present': True, 'count': 1 },
#     'b': { 'present': True, 'count': 2 },
#     'c': { 'present': False, 'count': 0 },
#     'd': { 'present': True, 'count': 1 },
#     'e': { 'present': False, 'count': 0 },
# }

# do this with a comprehension



# Remove all duplicate letters from a string, keeping only the first occurrence.
# The input is restricted to contain no numerals and only words containing the English alphabet letters.

# You may not use a set.

def remove_duplicates(string):
    new_string = ''
    for char in string:
        if char.lower().count(string.lower()) == 1:
            new_string += char
        elif char.lower() not in new_string.lower():
            new_string += char

    
    return new_string
            

# Tests
print(remove_duplicates("Launch School") == "Launch So")
print(remove_duplicates("CodeWars can't Load Today") == "CodeWars n'tLy")
print(remove_duplicates("success") == "suce")

