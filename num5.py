from functools import reduce
my_list = [el for el in range(100, 1001) if not(el % 2)]
print(reduce(lambda a, b: a*b, my_list))
