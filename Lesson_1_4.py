# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
a = 1
while a == int(a):
    try:
        n = int(input("Введите целое положительное число: "))
        if n > 0:
            break
        else:
            print("Ошибка ввода - значение числа должно быть положительным")
    except ValueError:
        print("Ошибка ввода - значение должно быть числом")

max_n = n % 10
while n > 1:
    last_n = n % 10
    n = n // 10
    if max_n < 9:
        if last_n > max_n:
            max_n = last_n
print(f"Наибольшая цифра во введенном числе = {max_n}")
