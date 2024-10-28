def triangle(side1, side2, side3):
    perimeter = side1 + side2 + side3
    shortest = min(side1, side2, side3)
    longest = max(side1, side2, side3)
    middle = perimeter - longest - shortest

    if is_valid(shortest, middle, longest):
        return get_triangle_type(shortest, middle, longest)
    else:
        return 'invalid'
    
def is_valid(shortest, middle, longest):
    return shortest > 0 and shortest + middle > longest

def get_triangle_type(shortest, middle, longest):
    if shortest == middle == longest:
        return 'equilateral'
    elif shortest == middle or shortest == longest or middle == longest:
        return 'isosceles'
    
    return 'scalene'
    

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == 'invalid'  )    # True
print(triangle(3, 1, 1) == "invalid")      # True