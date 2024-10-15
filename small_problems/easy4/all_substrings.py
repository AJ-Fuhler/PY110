def leading_substrings(string):
    substring_list = []

    for idx in range(1, len(string) + 1):
        substring_list.append(string[:idx])

    return substring_list


def substrings(string):
    all_substrings = []
    for idx in range(len(string)):
        all_substrings += leading_substrings(string[idx:])
    
    return all_substrings

expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True