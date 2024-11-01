lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

multiples_of_three = [
    [number for number in numbers if number % 3 == 0] for numbers in lst
]

print(multiples_of_three)