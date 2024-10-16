VOWELS = 'aeiouAEIOU'

def remove_vowels(lst_strings):
    result = []

    for string in lst_strings:
        new_string = ''
        for char in string:
            if char not in VOWELS:
                new_string += char
        result.append(new_string)
    return result
   




# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True