class ComplexNum:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return ComplexNum(self.real * other.real, self.imag * other.imag)

    def __str__(self):
        return f'{self.real} + {self.imag}i '

a = ComplexNum(2, 7)
print(a)
b = ComplexNum(5, 8)
print(b)
print(a + b)
print(a * b)
