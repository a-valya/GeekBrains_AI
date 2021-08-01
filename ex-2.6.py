goods = []
i = 0
flag = 'Да'
while flag == 'Да' or flag == 'да':
    name_value = input('введите название товара: ')
    cost_value = input('введите цену товара: ')
    quantity_value = input('введите количество товара: ')
    units_value = input('введите единицы измерения товара: ')
    param = {
            'name':  name_value,
            'cost': cost_value,
            'quantity': quantity_value,
            'units': units_value
            }
    new_good = (i, param)
    goods.append(new_good)
    print(goods)
    flag = input('добавить еще товар? Да/Нет ')
    i += 1

analytics = {}
names = []
costs = []
quantity_analitics = []
units_analytics = []
for good in goods:
    names.append(good[1].get('name'))
    costs.append(good[1].get('cost'))
    quantity_analitics.append(good[1].get('quantity'))
    units_analytics.append(good[1].get('units'))
    analytics.update({'names': set(names), 'costs': set(costs), 'quantity': set(quantity_analitics), 'units': set(units_analytics)})
print(analytics)
