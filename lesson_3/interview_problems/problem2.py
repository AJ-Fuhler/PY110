def minimum_sum(numbers):
    if len(numbers) < 5:
        return None
    
    smallest_sum = sum(numbers[:5])

    for idx in range(1, len(numbers) - 4):
        if sum(numbers[idx:idx + 5]) < smallest_sum:
            smallest_sum = sum(numbers[idx:idx + 5])

    
    return smallest_sum

print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)