from time import sleep


class TrafficLight:
    def __init__(self, color='красный'):
        self.__color = color

    def running(self):
        colors_time = {'красный': 7, 'желтый': 2, 'зеленый': 5}
        for num, color in enumerate(colors_time.keys()):
            self.__color = color
            print(f'сейчас горит {self.__color} свет')
            sleep(colors_time[color])


my_traffic_light = TrafficLight()
my_traffic_light.running()
