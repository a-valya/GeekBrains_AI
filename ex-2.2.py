i = 0
ls = []
print('для завершения ввода элементов введите stop')
while 1:
    element_value = input(f'введите элемент №{i}: ')
    if element_value == 'stop':
        break
    else:
        ls.append(element_value)
        i += 1

for num, el in enumerate(ls):
    # if num % 2 == 0:
    #     a = el
    #     try:
    #         ls[num] = ls[num + 1]
    #         ls[num + 1] = a
    #     except IndexError:
    #         pass

    # потом прочитала методичку...

    if num % 2 == 0:
        try:
            ls[num], ls[num + 1] = ls[num + 1], ls[num]
        except IndexError:
            pass
for e in ls:
    print(e)
