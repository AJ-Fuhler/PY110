def rotate_rightmost_digits(number, count):
    digits_list = list(str(number))
    digits_list.append(digits_list.pop(-count))

    return int(''.join(digits_list))

def max_rotation(number):
    for count in range(len(str(number)), 1, -1):
        number = rotate_rightmost_digits(number, count)
    
    return number


print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True