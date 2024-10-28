def sum_square_difference(number):
    sum_num = 0
    for num in range(1, number + 1):
        sum_num += num
    square_sum = sum_num ** 2

    sum_square = 0
    for num in range(1, number + 1):
        sum_square += num ** 2

    return square_sum - sum_square

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True


