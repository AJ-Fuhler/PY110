VOWELS = 'aeiouAEIOU'

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

def create_list_of_vowels(dct):
    result = []
    for value in dct.values():
        for word in value:
            for char in word:
                if char in VOWELS:
                    result += char
    
    return result

list_of_vowels = create_list_of_vowels(dict1)

print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

list_of_vowels = [char for value in dict1.values()
                       for word in value
                       for char in word
                       if char in VOWELS]

print(list_of_vowels)