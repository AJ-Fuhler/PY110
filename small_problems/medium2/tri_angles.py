def triangle(angle1, angle2, angle3):
    if is_valid(angle1, angle2, angle3):
        return get_triangle_type(angle1, angle2, angle3)
    else:
        return 'invalid'



def is_valid(angle1, angle2, angle3):
    if min(angle1, angle2, angle3) <= 0:
        return False
    elif sum([angle1, angle2, angle3]) != 180:
        return False
    
    return True

def get_triangle_type(angle1, angle2, angle3):
    if angle1 == 90 or angle2 == 90 or angle3 == 90:
        return 'right'
    elif angle1 < 90 and angle2 < 90 and angle3 < 90:
        return 'acute'
    else:
        return 'obtuse'
    

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True
