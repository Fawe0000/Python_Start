class Worker:

    def __init__(self, name, surname, position, income={"оклад": 0, "премия": 0}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(f'Должность "{self.position}" занимает {" ".join([self.name, self.surname])}')

    def get_total_income(self):
        print(
            f'Доход сотрудника "{self.position}" составляет: {self._income.get("оклад") + self._income.get("премия")}')
        print(f"----*" * 20)


staff1 = Position("Иван", "Петров", "Холоп", {"оклад": 100, "премия": 150})
staff1.get_full_name()
staff1.get_total_income()

staff2 = Position("Сидор", "Кузнецов", "Приказчик", {"оклад": 500, "премия": 800})
staff2.get_full_name()
staff2.get_total_income()

staff3 = Position("Марфа", "Посадница", "Барыня", {"оклад": 0, "премия": 8500})
staff3.get_full_name()
staff3.get_total_income()
