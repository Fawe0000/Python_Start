class Road:

    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def calc_mass(self, ud_massa=25, t_polot=5):
        massa_polot = self._lenght * self._width * ud_massa * t_polot / 1000
        print(f"Для покрытия всего дорожного полотна, имеющего характеристики:")
        print(f"Длина = {self._lenght}, метров;")
        print(f"Ширина = {self._width}, метров;")
        print(f"Толщина = {t_polot}, сантиметров;")
        print(f"Удельный вес одного кв метра толщиной в 1 см = {ud_massa};")
        print(f"Необходим объем асфальта, общей массой = {round(massa_polot)} тонн;")
        print(f"----*" * 20)


while True:
    try:
        print(
            f"Для рассчета массы асфальта, необходимого для покрытия дорожного полотна,\nвведите значения лины и ширины дороги.\nB противном случае, введите любой символ")
        m = Road(int(input("Введите длину: ")), int(input("Введите ширину: ")))
        m.calc_mass()
    except ValueError:
        print(f'Завершение без расчета')
        break
