def is_balanced(s):
    opening_characters = []

    closing = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in s:
        if char in closing.values():
            opening_characters.append(char)
        elif char in closing.keys():
            if closing[char] in opening_characters:
                opening_characters.remove(closing[char])
            else:
                return False
        elif char in ["'", '"']:
            if char not in opening_characters:
                opening_characters.append(char)
            else:
                opening_characters.remove(char)
    
    return not opening_characters





print(is_balanced("What [is] this?") == True)
print(is_balanced("What is} this?") == False)
print(is_balanced("What {is this?") == False)
print(is_balanced("({What} (is this))?") == True)
print(is_balanced("((What)) (is this))?") == False)
print(is_balanced("Hey!") == True)
print(is_balanced(")Hey!(") == False)
print(is_balanced("What ({is]}) up(") == False)
    
