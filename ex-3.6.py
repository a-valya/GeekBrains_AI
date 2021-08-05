# def int_func(str):
#     return str.title()

def main():
    str = (input('введите строку: ')).split()
    str = map(lambda str: str.title() , str)
    str = ' '.join(str)
    print(str)

main()
