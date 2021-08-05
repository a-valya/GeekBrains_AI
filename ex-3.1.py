def division(num1, num2):
    """  возвращает результат деления num1 на num2
    принимает два числовых аргумента num1, num2
    num1 - делимое, num2 - делитель
    """
    return num1/num2

def main():
    first_num = float(input('ведите делимое: '))
    second_num = float(input('ведите делитель: '))
    while second_num == 0:
        second_num = float(input('деление на ноль!\nвведите другой делитель: '))
    print(division(first_num,second_num))

main()


