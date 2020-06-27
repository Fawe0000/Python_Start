try:
    with open("text_3.txt", "r", encoding="utf-8") as my_file:
        k_str = 0
        summ_okl = 0
        prem = 0
        list_str = []
        for line in my_file:
            list_str = line.split(' ')
            prem = float(list_str[1])
            if prem < 20000:
                print(f"Сотрудник {list_str[0]} имеет оклад {list_str[1]}")
            k_str += 1
            summ_okl += prem

        print(f'\n Средний оклад всех  {k_str} сотрудников составляет {round(summ_okl / k_str, 2)}')
except IOError:
    print("Error")
else:
    print("Все так!")
