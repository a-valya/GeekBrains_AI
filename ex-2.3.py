# через dict

# month = input('введите номер месяца: ')
# times_of_year = \
# {
#     '1': 'winter',
#     '2': 'winter',
#     '3': 'spring',
#     '4': 'spring',
#     '5': 'spring',
#     '6': 'summer',
#     '7': 'summer',
#     '8': 'summer',
#     '9': 'autumn',
#     '10': 'autumn',
#     '11': 'autumn',
#     '12': 'winter'
# }
# time_of_year = times_of_year.get(month)
# print(time_of_year)

# через list

month = int(input('введите номер месяца: '))
times_of_year = [
    'winter',
    'winter',
    'spring',
    'spring',
    'spring',
    'summer',
    'summer',
    'summer',
    'autumn',
    'autumn',
    'autumn',
    'winter'
]
print(times_of_year[month])