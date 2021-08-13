subjects_dict = {}
keys_list = []
digits_list = []  # список чисел, отражающих кол-во занятий каждого типа для предмета
values_list = []
pos = 0           # начало поиска чисел

with open('subjects.txt', 'r', encoding='utf-8') as f_sub:

    for line in f_sub.readlines():

        new_key = ''
        for num, char in enumerate(line):
            if char == ':':
                keys_list.append(new_key)
                pos = num
                break
            new_key += char

        new_digit = ''
        for char in line[pos:]:
            if char.isdigit():
                new_digit += char
            elif new_digit:
                digits_list.append(float(new_digit))
                new_digit = ''

        value = 0
        for digit in digits_list:
            value += digit

        values_list.append(value)
        digits_list = []

for i in range(len(keys_list)):
    subjects_dict.update({keys_list[i]: values_list[i]})
print(subjects_dict)



