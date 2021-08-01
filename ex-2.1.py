ls = [
    34,
    True,
    7.9,
    'this is string',
    ['this' 'is' 'list'],
    ('this', 'is', 'tuple'),
    {'this', 'is', 'set'},
    {'name': 'John', 'surname': 'Lennon'},
    b'this is bytes',
    None
]
for elem in ls:
    print(type(elem))
