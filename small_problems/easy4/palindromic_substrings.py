def leading_substrings(string):
    return [string[:idx] for idx in range(1, len(string) + 1)]

def substrings(string):
    all_substrings = []
    for idx in range(len(string)):
        all_substrings += leading_substrings(string[idx:])
    
    return all_substrings

def palindromes(string):
    list_of_substrings = substrings(string)
    list_of_palindromes = []
    
    for substring in list_of_substrings:
        if len(substring) > 1:
            if substring == substring[::-1]:
                list_of_palindromes.append(substring)

    return list_of_palindromes

# or

def palindromes(string):
    return [substring for substring in substrings(string)
                      if len(substring) > 1
                      if substring == substring[::-1]]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True