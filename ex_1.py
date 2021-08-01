# № 1
int_num = 10
fl_num = int_num / 3
logical = 10 < 3
user_num = input('введите число: ')
print(f'Вы ввели число {user_num}')
user_name = input('Как Вас зовут? ')
print('Hello {}!'.format(user_name))

# № 2

user_time = int(input('Введите время в секундах: '))
seconds = user_time % 60

user_time = user_time - seconds
user_time = user_time // 60 # в минутах

hours = user_time // 60
minutes = user_time % 60

print(f'время: {hours} : {minutes} : {seconds}')

# № 3

n = input('Введите число: ')
nn = n + n
nnn = n * 3

rezult = int(n) + int(nn) + int(nnn)
print(rezult)

# № 4

user_number = int(input('Введите число: '))
max = 0
while user_number:
    new_digit = user_number % 10
    if  max < new_digit:
        max = new_digit
    user_number = user_number // 10
print(max)

# № 5

revenue = int(input('введите выручку: '))
expenses = int(input('введите расходы: '))
rez = revenue - expenses
if rez > 0:
    print (f'ваша прибыль составила{abs(rez)}')
    # profitability = rez /revenue # рентабельность
    print(f'рентабельность: {rez /revenue} ')
    staff_quantity = int(input('введите численность сотрудников: '))
    print(f'прибыль фирмы в расчете на одного сотрудника: {rez / staff_quantity} ')
else:
    print(f'ваш убыток составил {abs(rez)}')

# № 6

a = int(input('введите а: '))
b = int(input('введите b: '))
day = 1
while a < b:
    a = a + 0.1 * a
    day = day + 1
print(day)
