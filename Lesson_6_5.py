class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(" Метод отрисовки ")


class Pen(Stationery):
    def draw(self):
        print(f' Метод отрисовки Ручки "{self.title}"')


class Pencil(Stationery):
    def draw(self):
        print(f' Метод отрисовки Карандаша "{self.title}"')


class Handle(Stationery):
    def draw(self):
        print(f' Метод отрисовки Маркера "{self.title}"')


Handle("Brauberg").draw()
Pencil('Koh-I-Nor').draw()
Pen('Bic').draw()
