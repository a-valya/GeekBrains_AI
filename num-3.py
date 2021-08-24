class TypeErr(Exception):
    def __init__(self, txt):
        self.txt = txt

li = []
while True:
    el = input('введите новый элемент списка или Q для выхода: ')
    if el == 'Q':
        break
    try:
        if not el.isdigit():
            raise TypeErr('Вы ввели не число! ')
        el = int(el)
    except TypeErr as err:
        print(err)
    else:
        li.append(el)

print('Ваш список: ', li)
