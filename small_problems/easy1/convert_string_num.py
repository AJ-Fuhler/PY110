def string_to_integer(int_str):
    result = 0
    multiplier = 1

    for num in int_str[::-1]:
        num = HEXA_DIGITS[num]
        result += num * multiplier
        multiplier *= 10
    
    return result


HEXA_DIGITS = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15
}

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True

def hexadecimal_to_integer(int_str):
    result = 0
    exponent = 0
    
    for num in int_str[::-1].lower():
        num = HEXA_DIGITS[num]
        result += num * (16 ** exponent)
        exponent += 1
    
    return result

print(hexadecimal_to_integer('4D9f') == 19871)  # True