def count_max_adjacent_consonants(string):
    string = string.replace(' ', '')
    max_consonant_count = 0
    adjacent_consonant_string = ''
    consonants = 'bcdfghjklmnpqrstvwxyz'

    for char in string:
        if char in consonants:
            adjacent_consonant_string += char
            if len(adjacent_consonant_string) > max_consonant_count:
                if len(adjacent_consonant_string) > 1:
                    max_consonant_count = len(adjacent_consonant_string)
        else: 
            if len(adjacent_consonant_string) > max_consonant_count:
                if len(adjacent_consonant_string) > 1:
                    max_consonant_count = len(adjacent_consonant_string)
            adjacent_consonant_string = ''

    return max_consonant_count

print(count_max_adjacent_consonants('dddaa'))       # 3
print(count_max_adjacent_consonants('ccaa'))        # 2
print(count_max_adjacent_consonants('baa'))         # 0
print(count_max_adjacent_consonants('aa'))          # 0
print(count_max_adjacent_consonants('rsta fgd jecc ')) # 4



def sort_by_consonant_count(input_list):
    return sorted(input_list, key=count_max_adjacent_consonants, reverse=True)
    


my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']