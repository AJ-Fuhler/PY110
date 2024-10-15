def reverse_list(lst):
    reversed_list = []
    for idx in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[idx])
    
    lst += reversed_list

    for idx in range(len(lst) // 2):
        lst.pop(0)
    
    
    return lst

# or

def reverse_list(lst):
    for i in range(len(lst)):
        lst.insert(i, lst.pop())
    return lst



list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True FALSE
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True FALSE
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True