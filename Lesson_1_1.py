a = 1
while a == int(a):
    try:
        name = input("Введите ваше имя: ")
        a = int(name)
        print("Имя не может быть числом ", "%.2f" % int(name))
    except ValueError:
        try:
            name = float(name)
            print("Имя не может быть числом ", "%.2f" % name)
        except ValueError:
            print("Здравствуйте,", "%s" % name)
            a = 1.25
            break
    print("У вас ошибка ввода!")

while a != int(a):
    try:
        stage = input("Введите возраст (полных лет): ")
        stage = int(stage)
        print("Ваш возраст не менее %06d месяцев" % (int(stage)*12))
        a = 1
    except ValueError:
        print("Ошибка ввода - значение возраста должно быть числом")
        a = 1.25