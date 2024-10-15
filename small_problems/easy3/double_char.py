def repeater(string):
    return ''.join([char * 2 for char in string])

print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

CONSONANTS = 'bcdfghjklmnpqrstvwxyz'

def double_consonants(string):
    new_string = ''

    for char in string:
        if char.lower() in CONSONANTS:
            new_string += char * 2
        else:
            new_string += char

    return new_string


# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")