rus_numerals = ['один', 'два', 'три', 'четыре']
with open('text_4.txt', 'r') as f_en, open('text_4_rus', 'w', encoding='utf-8') as f_rus :
    for num, line in enumerate(f_en.readlines()):
        new_str = rus_numerals[num]
        for char in line:
            if not char.isalpha():
                new_str += char
        f_rus.write(new_str)
