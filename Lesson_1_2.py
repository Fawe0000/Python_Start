a = 1
while a == int(a):
    try:
        input_sek = input("Введите время в секундах: ")
        sek = float(input_sek)
        hh = sek//3600
        mm = (sek-hh*3600)//60
        ss = sek-hh*3600-mm*60
        print("В привычном виде, указанное время = %02d:%02d:%02d" % (hh, mm, ss))
        a = 1.25
    except ValueError:
        print("Ошибка ввода - значение должно быть числом")
        a = 1