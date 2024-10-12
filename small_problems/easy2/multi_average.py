def multiplicative_average(lst):
    multiplied_num = 1
    for current_num in lst:
        multiplied_num *= current_num
    
    return f'{multiplied_num / len(lst):.3f}'


# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")