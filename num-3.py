class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        sum = 0
        for value in map(int, self._income.values()):
            sum += value
        return sum


Tom = Position('Tom', 'Smith', 'director', 30500, 500)
print(Tom.surname)
print(Tom.get_full_name())
print(Tom.get_total_income())
