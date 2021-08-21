class Matrix:
    def __init__(self, st, col, *args):
        self.st = str
        self.col = col
        self.vectors = []
        if args:
            for arg in args:
                for ar in arg:
                    ar = map(str, ar)
                    self.vectors.append(ar)
        else:
            for i in range(st):
                vec = input(f'введите элементы строки №{i + 1}, разделяя их пробелами: ')
                self.vectors.append(vec.split())

    def __str__(self):
        matrix_str = []
        for vector in self.vectors:
            matrix_str.append(' '.join(vector))
        matrix_str = '\n'.join(matrix_str)
        return matrix_str

    def __add__(self, other):
        while True:
            if self.col == other.col and self.st == other.st:
                new_m = []
                for num_vec, vector in enumerate(self.vectors):
                    new_m_vector = []
                    for num_el, el in enumerate(vector):
                        new_m_vector.append(int(el) + int(other.vectors[num_vec][num_el]))
                    new_m.append(new_m_vector)
            return Matrix(self.st, self.col, new_m)
        else:
            print(' разные размерности матриц! ')

print('для матрицы А ')
a = Matrix(2, 2)
print('для матрицы В ')
b = Matrix(2, 2)
c = a + b
print('A + B = \n', c)


