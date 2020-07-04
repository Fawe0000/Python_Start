class Org_Cell:

    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Org_Cell(self.num + other.num)

    def __sub__(self, other):
        return Org_Cell(self.num - other.num) if self.num > other.num else "Ошибка, такое вычитание клиеток невозможно"

    def __mul__(self, other):
        return Org_Cell(self.num * other.num)

    def __truediv__(self, other):
        return Org_Cell(self.num // other.num) if other.num != 0 else "Ошибка, такое на ноль делить нельзя"

    def __str__(self):
        return f"{self.num}"

    def make_order(self, ci_row):
        my_list = "*" * self.num
        for i in range(self.num // ci_row + 1):
            print(my_list[i * ci_row:i * ci_row + ci_row])


cell_line_length = 9  # длина строки вывода ячеек клетки
c_1 = Org_Cell(15)
c_2 = Org_Cell(24)
c_3 = Org_Cell(4)
c_0 = Org_Cell(0)
c_10 = Org_Cell(34)

print(f'Сложение органических клеток {c_1} + {c_2} = {c_1 + c_2}')
(c_1 + c_2).make_order(cell_line_length)
input("Нажмите клавишу ввода")

print(f'Вычитание органических клеток {c_2} - {c_3} = {c_2 - c_3}')
(c_2 - c_3).make_order(cell_line_length)
input("Нажмите клавишу ввода")

print(f'Деление органических клеток {c_1} / {c_0} = {c_1 / c_0}')
input("Нажмите клавишу ввода")

print(f'Деление органических клеток {c_10} / {c_3} = {c_10 / c_3}')
(c_10 / c_3).make_order(cell_line_length)
input("Нажмите клавишу ввода")

print(f'Умножене органических клеток {c_10} * {c_2} = {c_10 * c_2}')
print('Такая большая клетка и вся шире!')
cell_line_length = 58
(c_10 * c_2).make_order(cell_line_length)
input("Нажмите клавишу ввода")

print("Спасибо, это всё!")
