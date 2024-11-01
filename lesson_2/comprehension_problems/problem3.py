lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

print([sorted(sublist, key=str) for sublist in lst])