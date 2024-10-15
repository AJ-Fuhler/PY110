def leading_substrings(string):
    substring_list = []

    for idx in range(1, len(string) + 1):
        substring_list.append(string[:idx])

    return substring_list

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

def leading_substrings(string):
    return [string[:idx] for idx in range(1, len(string) + 1)]

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])