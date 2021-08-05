def user_data(**kwargs):

    """ принимает любое количество параметров, описывающих данные о пользователе
    возвращает данные о пользователе одной строкой в формате словаря"""

    return kwargs

def main():
    print(user_data(name = 'Ivan', surname = 'Ivanov', year = '1990', email = 'example@gmail.ru', phone_number = '89999999999'))

main()