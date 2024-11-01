dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}


def transform_value(value):
    if value['type'] == 'vegetable':
        return value['size'].upper()
    else:
        return [color.capitalize() for color in value['colors']]

result = [transform_value(value) for value in dict1.values()]

print(result)