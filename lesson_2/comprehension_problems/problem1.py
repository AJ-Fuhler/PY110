munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

total = 0
for person, info in munsters.items():
    if info['gender'] == 'male':
        total += info['age']

print(total)

total = sum([info['age'] for person, info in munsters.items()
                         if info['gender'] == 'male'])

print(total)