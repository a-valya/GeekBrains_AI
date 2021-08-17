class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} едет')

    def stop(self):
        print(f'{self.name} останавливается')

    def turn(self, direction):
        print(f'{self.name} поворачивает {direction}')

    def show_speed(self):
        print('скорость движения:',self.speed)

class TownCar(Car):
    def show_speed(self):
        print('скорость движения:', self.speed)
        if self.speed > 60:
            print('Вы превышаете допустимую скорость')

class SportCar(Car):
    def engine_sound(self):
        print('VROOM VROOOM !!!')

class WorkCar(Car):
    def show_speed(self):
        print('скорость движения:', self.speed)
        if self.speed > 40:
            print('Вы превышаете допустимую скорость')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


ford = TownCar(65, 'grey', 'Ford')
bugatti = SportCar(450, 'blue', 'Bugatti')
komatsu = WorkCar(47, 'yellow', 'Komatsu')
uaz = PoliceCar(90, 'white', 'UAZ')

ford.go()
ford.show_speed()
bugatti.go()
bugatti.engine_sound()
komatsu.turn('направо')
komatsu.show_speed()
komatsu.stop()
uaz.go()
uaz.show_speed()
print('этот уазик - полицейская машина? ', uaz.is_police)
print('этот бугатти - полицейская машина?', bugatti.is_police)
