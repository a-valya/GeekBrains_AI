def sum(str):
    """возвращает сумму чисел
    принимает один позиционный параметр - строку str, содержащую числа, разделенные пробелом
    """
    list = str.split()
    sum = 0
    for el in list:
        if el == 'q' or el == 'Q':
            break
        sum += int(el)
    return sum

def main():
    s = 0
    fl = 1
    while fl:
        str = input()
        for char in str:
            if char == 'q' or char == 'Q':
                fl = 0
        s += sum(str)
        print('sum = ',s)
    print('end')

main()