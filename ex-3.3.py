def my_func(f_num, s_num, th_num):
    """ возвращает сумму наибольших двух аргументов

    принимает три позиционных числовых аргумента:
    f_num, s_num, th_num
    """
    unwanted = min(f_num, s_num, th_num)
    result_list = [f_num, s_num, th_num]
    result_list.remove(unwanted)
    result = result_list[0] + result_list[1]
    return result

def main():
    print(my_func(5, 3, 4))

main()