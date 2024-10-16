def join_or(lst, delimiter=', ', final_delimiter='or'):
    result = ''
    
    for element in lst[:-2]:
        result += f'{element}{delimiter}'
    if len(lst) > 1:
        result += f'{lst[-2]} {final_delimiter} {lst[-1]}'
    elif len(lst) == 1:
        return str(lst[0])


    return result

print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"
        