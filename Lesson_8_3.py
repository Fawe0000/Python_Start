class My_num_class(Exception):
    def ch_num(ch_num):
        try:
            return float(ch_num)
        except ValueError:
            if ch_num != "Q":
                print("Ошибка! Вы ввели не число")


my_str = []
i = ""
while i.lower() != 'q':
    i = input("Введите число для заполнения списка, или 'q' для выхода: ")
    if My_num_class.ch_num(i):
        my_str.append(My_num_class.ch_num(i))
    print(my_str)
