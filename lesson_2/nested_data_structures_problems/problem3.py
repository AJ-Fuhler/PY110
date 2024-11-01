a = 2
b = [5, 8]
lst = [a, b] # [2, [5, 8]]

lst[0] += 2 # [4, [5, 8]]
lst[1][0] -= a # [4, [3, 8]]

# a == 2, integers are immutable and a was never reassigned. b = [3, 8], at
# line 6 we mutated the list referenced at lst[1], by reassigning the element
# at index 0 (5) to the evaluation of (5 - a) -> (5 - 2), which is 3. Both the
# element at lst[1] and b reference the same list object in memory. This is why
# we see the change in both b and within lst[1].

print(lst)
print(a)
print(b)

