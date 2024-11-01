lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

def incremented_values(dct):
    return {key: value + 1 for key, value in dct.items()}

incremented_value_list = [incremented_values(dct) for dct in lst]
print(incremented_value_list)

# or

new_lst = [{key: value + 1 for key, value in dictionary.items()}
                           for dictionary in lst]

print(new_lst)