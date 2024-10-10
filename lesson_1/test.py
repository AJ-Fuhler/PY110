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


print(count_max_adjacent_consonants('xxxaxx'))