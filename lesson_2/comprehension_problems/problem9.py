lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def all_even(lst):
        return all([number % 2 == 0 for number in lst])

def all_lsts_even(dct):
      return all([all_even(lst) for lst in dct.values()])


new_lst = [dct for dct in lst if all_lsts_even(dct)]

print(new_lst)