class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width
    def calc_weight(self, mass_per_one_sm, thickness):
        return self._Road__length * self._Road__width * mass_per_one_sm * thickness


leninsky_prospekt = Road(10000, 2000)
print(f'потребуется {leninsky_prospekt.calc_weight(25, 5)}т асфальта')
