user_str = input('введите строку: ')
separated_str = user_str.split()
for num, word in enumerate(separated_str):
    if len(word) > 10:
        print(f'{num} {word[:10]}')
    else:
        print(f'{num} {word}')
