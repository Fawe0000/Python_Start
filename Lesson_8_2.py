class DevZeroError(Exception):
    def __init__(self, txt):
        self.txt = txt

try:
    inp_ch = float(input("Введите числитель: "))
    inp_zn = float(input("Введите знаменатель: "))
    if inp_zn:
        raise DevZeroError("Ошибка! На ноль делить нельзя!")
    rez = inp_ch/inp_zn
except ValueError:
    print("Ошибка! Вы ввели не число")
except DevZeroError as err:
    print(err)
else:
    print(f"Все хорошо. Ваше число: {rez}")
