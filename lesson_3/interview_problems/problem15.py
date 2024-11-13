"""
Create a function that takes a string argument that consists entirely of
numeric digits and computes the greatest product of four consecutive digits in
the string. The argument will always have more than 4 digits.

P:
input: string of digits
output: integer representing greatest product of four consecutive digits from
string

explicit:
- argument will always have more than 4 digits.
- return greatest product of four consecutive digits from string.

E:

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

D:
- list containing all possible products of four consecutive digits
- max function to capture highest value in that list
- looping

A:
- given a string of digits
- product_list = []
- for each index from 0 through length of string - 4
  - append to product_list: (string[index] * string[index + 1] * string[index + 2]
    * string[index + 4])

- return max value in product_list




"""

def greatest_product(digits):
    product_list = []
    for idx in range(len(digits) - 3):
        product_list.append(int(digits[idx]) * int(digits[idx + 1]) * int(digits[idx + 2])
                            * int(digits[idx + 3]))
    
    return max(product_list)

def greatest_product(digits):
    product_list = []
    for idx in range(len(digits) - 3):
        product = 1
        for next_index in range(idx, idx + 4):
            product = int(digits[next_index]) * product

        product_list.append(product)

    return max(product_list)    


print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6