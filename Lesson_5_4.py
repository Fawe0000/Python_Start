try:
    with open("text_4.txt", "r", encoding="utf-8") as my_file:
        new_file = open("text_4w.txt", "w+", encoding="utf-8")
        my_chisl = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть','семь','восемь','девять']
        prem = 0
        list_str = []
        for line in my_file:
            list_str = line.split(' ')
            prem = int(list_str[2])
            list_str[0] = my_chisl[prem]
            print(f" {' '.join(list_str)}", file=new_file)
except IOError:
    print("Error")
else:
    new_file.seek(0)
    print(f'Содерджимое файла "{new_file.name}:')
    print(new_file.read())