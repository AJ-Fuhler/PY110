def calculate_leftover_blocks(number_of_blocks):
    layer_number = 1

    while number_of_blocks >= 0:
        if number_of_blocks >= layer_number ** 2:
            number_of_blocks -= (layer_number ** 2)
            layer_number += 1
        else:
            return number_of_blocks
    
    

print(calculate_leftover_blocks(0) == 0)  # True
print(calculate_leftover_blocks(1) == 0)  # True
print(calculate_leftover_blocks(2) == 1)  # True
print(calculate_leftover_blocks(4) == 3)  # True
print(calculate_leftover_blocks(5) == 0)  # True
print(calculate_leftover_blocks(6) == 1)  # True
print(calculate_leftover_blocks(14) == 0) # True