class Data:
    def __init__(self, date):
        self.date = date

    @classmethod           # не поняла, для чего здесь можно использовать ссылку на класс (
    def convert_to_digit(cls, date):
        return list(map(int, date.split('-')))

    @staticmethod
    def is_valid(date):
        date = date.split('-')
        for num, part in enumerate(date):
            try:
                if num == 0 and int(part) > 31:
                    return 0
                elif num == 1 and int(part) > 12:
                    return 0
            except ValueError:
                return 0
        return 1

print(Data.convert_to_digit('10-09-2021'))
print(Data.is_valid('10-9!-2021'))
