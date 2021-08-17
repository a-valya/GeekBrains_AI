class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('запуск отрисовки ручкой.')


class Pencil(Stationery):
    def draw(self):
        print('запуск отрисовки карандашом.')


class Handle(Stationery):
    def draw(self):
        print('запуск отрисовки маркером.')


my_pen = Pen('Ручка')
my_pencil = Pencil('Карандаш')
my_handle = Handle('Маркер')

my_pen.draw()
my_pencil.draw()
my_handle.draw()
