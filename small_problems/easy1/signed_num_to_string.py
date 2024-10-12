DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(number):
    result = ''

    while number > 0:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result

    return result or '0'

def signed_integer_to_string(number):
    if number < 0:
        number = abs(number)
        return '-' + integer_to_string(number)
    elif number > 0:
        return '+' + integer_to_string(number)
    else:
        return '0'
    
print(signed_integer_to_string(4321) == "+4321")  # True
print(signed_integer_to_string(-123) == "-123")   # True
print(signed_integer_to_string(0) == "0")         # True