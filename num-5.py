with open('numbers.txt', 'w') as f_num:
    str_numbers = input('введите числа, разделенные пробелом: ')
    f_num.write(str_numbers)

list_numbers = []

with open('numbers.txt', 'r') as f_num:
    new_digit = ''
    for char in f_num.readline():
        if char.isdigit():
            new_digit += char
        elif char == ' ':
            list_numbers.append(new_digit)
            new_digit = ''
list_numbers.append(new_digit)
list_numbers = list(map(float, list_numbers))
sum = 0
for num in list_numbers:
    sum += num
print('сумма чисел: ', sum)
