from sys import argv
rate = int(argv[1])
time = int(argv[2])
bonus = int(argv[3])
salary = (time * rate) + bonus
print('Вы заработали: ', salary)