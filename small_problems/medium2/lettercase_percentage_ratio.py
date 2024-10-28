def letter_percentages(string):
    lowercase = ''
    uppercase = ''
    neither = ''

    for char in string:
        if char.islower():
            lowercase += char
        elif char.isupper():
            uppercase += char
        else:
            neither += char

    lowercase_percentage = (len(lowercase) / len(string)) * 100
    uppercase_percentage = (len(uppercase) / len(string)) * 100
    neither_percentage = (len(neither) / len(string)) * 100

    dct = {}

    dct['lowercase'] = f'{lowercase_percentage:.2f}'
    dct['uppercase'] = f'{uppercase_percentage:.2f}'
    dct['neither'] = f'{neither_percentage:.2f}'

    return dct


expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)