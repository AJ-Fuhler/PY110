def palindrome_substrings(s):
    result = []
    substrings_list = substrings(s)

    for substring in substrings_list:
        if is_palindrome(substring):
            result.append(substring)
    
    return result


def substrings(s):
    result = []
    start_index = 0
    
    while start_index <= len(s) - 2:
        num_chars = 2
        while num_chars <= len(s) - start_index:
            result.append(s[start_index:num_chars + start_index])
            num_chars += 1
        start_index += 1
    
    return result


def is_palindrome(substring):
    return substring == substring[::-1]



print(palindrome_substrings("abcddcbA"))   # ["bcddcb", "cddc", "dd"]
print(palindrome_substrings("palindrome")) # []
print(palindrome_substrings(""))           # []
print(palindrome_substrings("repaper"))    # ['repaper', 'epape', 'pap']
print(palindrome_substrings("supercalifragilisticexpialidocious")) # ["ili"]