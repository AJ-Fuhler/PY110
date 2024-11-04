import random
HEXADECIMAL = 'abcdef0123456789'

def generate_uuid():
    SECTIONS = [8, 4, 4, 4, 12]
    return '-'.join([create_section(section_length) 
                       for section_length in SECTIONS])


def create_section(section_length):
    return ''.join([random.choice(HEXADECIMAL) for _ in range(section_length)])


print(generate_uuid())

