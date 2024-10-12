def halvsies(original_list):
    if not original_list:
        return [[], []]
    if len(original_list) == 1:
        return [[original_list[0]], []]
    
    if len(original_list) % 2 == 0:
        center_index = len(original_list) // 2
    else: 
        center_index = (len(original_list) // 2) + 1
    
    lst1 = original_list[:center_index]
    lst2 = original_list[center_index:]

    return [lst1, lst2]




# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])

def halvsies(lst):
    half = (len(lst) + 1) // 2
    return [lst[:half], lst[half:]]

# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])