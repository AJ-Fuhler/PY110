def unique_sequence(numbers):
    new_lst = []
    for num in numbers:
        if new_lst:
            if num != new_lst[-1]:
                new_lst.append(num)
        else:
            new_lst.append(num)
    
    return new_lst

def unique_sequence(numbers):
    return [number
            for idx, number in enumerate(numbers)
            if idx == 0 or number != numbers[idx-1]]

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True
print(unique_sequence([]))