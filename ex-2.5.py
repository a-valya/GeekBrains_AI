rating = [6, 5, 5, 1, 1]
print('для завершения работы введите stop ')
new = input('введите новый элемент рейтинга: ')
while new != 'stop':

    try:
        new = int(new)

    except ValueError:
        print('недопутимое значение элемента!')
        new = input('введите новый элемент рейтинга: ')
        continue

    else:


        try:
            ind = rating.index(new)          # индекс первого элемента с таким же значением

        except ValueError:             # если нет таких элементов -----------------------------------

            if new >= rating[0]:              # если новый элемент больше самого первого
                rating.insert(0, new)
            elif new >= rating[-1]:            # если новый элемент нужно расположить внутри списка

                for num, elem in enumerate(rating):
                    if new > elem:
                        rating.insert(num, new)
                        break
# почему без этого break цикл становится бесконечным?
            #  разве он не должен закончиться на последнем элементе списка?

            else:                                 # если новый элемент меньше самого последнего
                rating.append(new)

        else:                                          # если есть элементы с таким же значением ----------------------

            count_of_similar = rating.count(new)           # количество элементов с этим значением
            position = ind + count_of_similar
            rating.insert(position, new)
    print(rating)
    new = input('введите новый элемент рейтинга: ')

