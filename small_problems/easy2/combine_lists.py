def interleave(lst1, lst2):
    return [item for pair in zip(lst1, lst2) for item in pair]

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True

def interleave(lst1, lst2):
    result = []
    zipped_list = zip(lst1, lst2)
    for item1, item2 in zipped_list:
        result.append(item1)
        result.append(item2)

    return result

print(interleave(list1, list2) == expected)