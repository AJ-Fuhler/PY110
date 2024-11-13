"""
Create a function that takes a list of integers as an argument. The function
should determine the minimum integer value that can be appended to the list so
the sum of all the elements equal the closest prime number that is greater than
the current sum of the numbers. For example, the numbers in [1, 2, 3] sum to 6.
The nearest prime number greater than 6 is 7. Thus, we can add 1 to the list to
sum to 7.

The list will always contain at least 2 integers.
All values in the list must be positive (> 0).
There may be multiple occurrences of the various numbers in the list.

input: list of integers
output: integer representing the number to add to the list to get to the
nearest prime number greater than the current sum of the input list.

Explicit:
- The list will always contain at least 2 integers.
- All values in the list must be positive (> 0)
- There may be multiple occurrences of the various numbers in the list
- return integer

implicit:
- 

E:

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

D:

- function that can determine whether a number is a prime number.
- 

A:

- given a list of integers
- result = 1
while True:
- if sum of list plus result is a prime:
  - return result
- else:
  result += 1

return result

is_prime:

- given a number:
- for divisor in a range from 2 through number - 1:
  - if number & divisor == 0:
    - return False

- return True


"""

def nearest_prime_sum(numbers):
    result = 1
    while True:
        if is_prime(sum(numbers) + result):
            return result
        else:
            result += 1


def is_prime(number):
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    
    return True

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)