import json
profit_list = []
company_names = []
ave = 0
positiv_profit = 0            # количество фирм с положительной прибылью
total_list = []
profit_dict = {}
with open('company.txt', 'r', encoding='utf-8') as f_com:
    for line in f_com.readlines():
        rev = ''              # выручка
        expen = ''         # расходы
        company_name = ''  # название компании
        pos = 0
        for num, char in enumerate(line):
            if char.isalpha():
                company_name += char
            elif company_name:
                pos = num
                break

        for num, char in enumerate(line[pos:]):
            if char.isdigit():
                rev += char
            elif rev:
                pos += num
                break

        for char in line[pos:]:
            if char.isdigit():
                expen += char

        profit = float(rev) - float(expen)
        profit_list.append(profit)
        company_names.append(company_name)

    for prof in profit_list:
        if prof > 0:
            ave += prof
            positiv_profit += 1

    ave /= positiv_profit
    print('прибыль компаний составила соответственно: ', profit_list)
    print('средняя прибыль равна ', ave)

for num, name in enumerate(company_names):
    profit_dict.update({name: profit_list[num]})

total_list.append(profit_dict)
total_list.append({'average_profit' : ave})

print(total_list)

with open('company.json', 'w') as f_json:
    json.dump(total_list, f_json)
