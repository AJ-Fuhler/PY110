def multiply_list(lst1, lst2):
    result = []
    for idx in range(len(lst1)):
        product = lst1[idx]* lst2[idx]
        result.append(product)
    
    return result

list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2) == [27, 50, 77])  # True

def multiply_list(lst1, lst2):
    zipped = zip(lst1, lst2)
    result = []
    for elem1, elem2 in zipped:
        result.append(elem1 * elem2)

    return result

print(multiply_list(list1, list2) == [27, 50, 77])  # True

def multiply_list(lst1, lst2):
    return [a * b for a, b in zip(lst1, lst2)]

print(multiply_list(list1, list2) == [27, 50, 77])  # True