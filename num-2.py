class ZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt

divisor = int(input('введите делитель: '))
try:
    if divisor == 0:
        raise ZeroDiv(' Деление на ноль! ')
    res = 10 / divisor
except ZeroDiv as error:
    print(error)
