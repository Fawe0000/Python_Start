a = 1
while a == int(a):
    try:
        n_string = input("Введите число 'n': ")
        n = int(n_string)
        nn = int(n_string+n_string)
        nnn = int(n_string+n_string+n_string)
        print(f"Расчет n+nn+nnn = {n+nn+nnn}")
        a = 1.25
    except ValueError:
        print("Ошибка ввода - значение должно быть числом")