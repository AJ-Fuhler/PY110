def next_featured(number):
    LARGEST_FEATURED_NUMBER = 9876543201
    if number >= LARGEST_FEATURED_NUMBER:
        return ("There is no possible number that "
         "fulfills those requirements.")
    
    for num in range(number + 1, LARGEST_FEATURED_NUMBER + 1):
        if is_featured(num):
            return num
        
    



def is_featured(number):
    if number % 7 == 0 and number % 2 == 1:
        string_num = str(number)
        if len(set(string_num)) == len(string_num):
            return True
        
    return False
    



print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(next_featured(9876543201) == error)       # True