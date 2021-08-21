class Cell:
    def __init__(self, count=1):
        self.count = count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count - other.count > 0:
            return Cell(self.count - other.count)
        else:
            print(f'Ошибка! разность количества ячеек меньше нуля! Возвращен первый переданный объект')
            return self

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        return Cell(self.count // other.count)

    def make_order(self, count_in_row):
        row_list = []
        j = 0
        for _ in range(self.count):
            j += 1
            if j == count_in_row:
                row_list.append('*' * j + '\n')
                j = 0
        row_list.append('*' * j)
        return ''.join(row_list)


a = Cell(15)
print(a.make_order(7))
b = Cell(5)
c = a + b
print(c.count)
c = a - b
print(c.count)
d = b - a
print(d.count)
c = a * b
print(c.count)
c = a / b
print(c.count)

