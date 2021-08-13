with open('test.txt', 'r') as f:
    str_count = 0
    words_count_list = []
    for line in f:
        str_count += 1

        if line:                      # если строка не пустая
            words_count = 1

            for chr in line:
                if chr == ' ':
                    words_count += 1
            words_count_list.append(words_count)

        else:
            words_count = 0


print('количество строк в файле: ',str_count)
print('количество слов в каждой из строк: ',words_count_list)