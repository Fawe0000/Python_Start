try:
    with open("file_1.txt", "r", encoding="utf-8") as my_file:
        k_str = 0
        k_symb = 0
        sum_simb = 0
        for line in my_file:
            k_str += 1
            k_symb = len(line)
            sum_simb += k_symb
            print(f'Строка {k_str} содержит {k_symb} символов')
        print(f'\n Всего файле "{my_file.name} содержит {k_str} строк и {sum_simb} символов')
except IOError:
    print("Error")
else:
    print("Ok")