with open('salary.txt', 'r', encoding='utf-8') as f:
    sal_list = []
    less_then_20k = []
    for line in f.readlines():
        sal = ''

        for char in line:
            if char.isdigit():
                sal += char

        if float(sal) < 20000:
            name = ''

            for char in line:
                if char.isalpha():
                    name += char
                else:
                    less_then_20k.append(name)
                    break

        sal_list.append(sal)
sal_list = list(map(float, sal_list))
ave = 0
for sal in sal_list:
    ave += sal
ave /= len(sal_list)
print('сотрудники, которым надо поднять зарплату: ', less_then_20k)
print('средняя величина дохода сотрудников: ', ave)
