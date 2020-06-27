from itertools import count
try:
    with open("file_1.txt", "r", encoding="utf-8") as my_file:
        print("для окончания ввода, введите пустую строку")
        for i in count(1):
            inp_symb = input(f'введите {i}-ю строку:')
            if inp_symb != "":
                my_file.write(inp_symb + "\n")
            else:
                break
        my_file.seek(0)
        print(f'Содерджимое файла "{my_file.name}:')
        print(my_file.read())
except IOError:
    print("Error")
else:
    print("Это всё!")