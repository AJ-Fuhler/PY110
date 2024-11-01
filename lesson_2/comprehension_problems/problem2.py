lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

new_lst = []
for inner_lst in lst:
    new_lst.append(sorted(inner_lst))

print(new_lst)

print([sorted(inner_lst) for inner_lst in lst])