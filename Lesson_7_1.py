class Matrix:
    def __init__(self, num):
        self.num = num
        self.my_str = ''

    def __str__(self):
        print(f'Распечатаем матрицу: {self.num}')
        for i in self.num:
            for e in range(len(i)):
                self.my_str += f"{i[e]:<6}"
            self.my_str += "\n"
        return self.my_str

    def __add__(self, other):
        try:
            add_num = []
            for j, i in enumerate(self.num):
                str_num = []
                for e in range(len(i)):
                    str_num.append(self.num[j][e] + other.num[j][e])
                add_num.append(str_num)
            return Matrix(add_num)
        except IndexError:
            return "Ошибка: Обе матрицы долджны иметь одинаковый размер"


m1 = Matrix([[1, 2, 3, 4, 5], [3, 4, 4, 4, 5], [3, 78, 65, 465, 5], [123, 654, 457, 45, 5]])
m2 = Matrix([[0, 122, 23, 40, 5], [31, 24, 64, 655, 2], [3, 8, 5, 6, 155], [1, 6, 127, 5, 85]])

print(m1)
print(m2)
print('Сложим две матрицы одинакового размера.')
print(m1 + m2)
