with open('new_file.txt', 'w') as f:
    while 1:
        new_str = input('введите следующую строку или нажмите Enter для завершения: ')
        if new_str:
            f.write(new_str + '\n')
        else:
            break
