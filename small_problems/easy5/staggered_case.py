# part 1

def staggered_case(string):
    new_string = ''
    for idx in range(len(string)):
        if idx % 2 == 0:
            new_string += string[idx].upper()
        else:
            new_string += string[idx].lower()
    
    return new_string




string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

# part 2

def staggered_case(string):
    new_string = ''
    count = 0
    
    for char in string:
        if char.isalpha() and count % 2 == 0:
            new_string += char.upper()
            count += 1
        else:
            new_string += char.lower()
            if char.isalpha():
                count += 1

    
    return new_string


string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True
