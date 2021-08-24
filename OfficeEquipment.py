class Err(Exception):
    def __init__(self, txt):
        self.txt = txt

class Store:
    dict_eq = {'Printer': 0, 'Scanner': 0, 'Xerox': 0}

    @classmethod
    def reception(cls, name, count=0):
        if count:
            cls.dict_eq.update({name: count})
            print(f'{name} принят на склад в количестве {count}шт. Текущее состояние склада: {cls.dict_eq}')
        else:
            if cls.dict_eq.get(name):
                count = cls.dict_eq.get(name) + 1
            else:
                count = 1
            cls.dict_eq.update({name: count})
            print(f'{name} принят на склад. Текущее состояние склада: {cls.dict_eq}')

    @classmethod
    def show_list_of_eq(cls):
        print(cls.dict_eq)


class OfficeEquipment:
    def __init__(self, color, id, name):
        self.color = color
        self.id = id
        self.name = name
        Store.reception(self.name)


class Printer(OfficeEquipment):
    def __init__(self, color, id, printing_type):
        self.printing_type = printing_type
        super().__init__(color, id, 'Printer')


    @staticmethod
    def printing():
        print(' печатаем на принтере... ')


class Scanner(OfficeEquipment):
    def __init__(self, color, id, dpi):
        super().__init__(color, id, 'Scanner')
        self.dpi = dpi

    @staticmethod
    def scanning():
        print('сканируем... ')


class Xerox(OfficeEquipment):
    def __init__(self, color, id, dpi):
        super().__init__(color, id, 'Xerox')
        self.dpi = dpi

    @staticmethod
    def xeroxing():
        print('делаем ксерокопию...')


a = Printer(color='black', id=1, printing_type='laz')
b = Printer(color='white', id=2, printing_type='st')
c = Scanner(color='black', id=1, dpi=9600)
d = Xerox(color='black', id=1, dpi=6400)

name = input('имя товара: ')
count = 0
while not count:
    try:
        count = input('количество товара: ')
        if not count.isdigit():
            count = 0
            raise Err('количество нужно ввести числом!')
    except Err as e:
        print(e)
    else:
        Store.reception(name, count)
