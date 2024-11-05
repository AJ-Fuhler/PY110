fib_nums = {
1: 1,
2: 1
}

def fibonacci(nth):
    if nth <= 2:
        return 1
    
    if nth in fib_nums:
        return fib_nums[nth]
    
    fib_nums[nth] = fibonacci(nth - 1) + fibonacci(nth - 2)
    return fib_nums[nth]


print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True