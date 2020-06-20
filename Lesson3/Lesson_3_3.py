"""Реализовать функцию my_func(),
которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов."""

# описываем функцию
def my_func(arg1, arg2, arg3):
    my_list = sorted((arg1, arg2, arg3), reverse=True)
    return sum([my_list[0], my_list[1]])

# описываем функию ввода и проверки корректности аргументов
def func_input(numbr):
    while True:
        try:
            imp_x = float(input(f"Введите {numbr}-й аргумент = "))
            break
        except ValueError:
            print(f'Ошибка! {numbr}-й аргумент должен быть числом')
    return float(imp_x)

print('-*-'*35)
print('реализуем функцию сортирующую суммирующую 2 наибольших из 3 введенных аргументов')
n1 = func_input(1)
n2 = func_input(2)
n3 = func_input(3)

print(f'Сумма двух наибольших введенных аргументов = {my_func(n1, n2, n3):.2f}')
