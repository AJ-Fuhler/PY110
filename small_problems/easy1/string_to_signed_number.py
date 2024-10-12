def string_to_signed_integer(int_str):
    result = 0
    multiplier = 1
    sign = '-' if int_str[0] == '-' else None
    if int_str[0] in ['-', '+']:
        int_str = int_str[1:]

    for num in int_str[::-1]:
        num = DIGITS[num]
        result += num * multiplier
        multiplier *= 10
    
    if sign == '-':
        return -result
    return result


DIGITS = {
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
}

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True


def string_to_integer(int_str):
    result = 0
    multiplier = 1

    for num in int_str[::-1]:
        num = DIGITS[num]
        result += num * multiplier
        multiplier *= 10
    
    return result


def string_to_signed_integer(int_str):
    match int_str[0]:
        case '-':
            return -string_to_integer(int_str[1:])
        case '+':
            return string_to_integer(int_str[1:])
        case _:
            return string_to_integer(int_str)
        


print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True

    