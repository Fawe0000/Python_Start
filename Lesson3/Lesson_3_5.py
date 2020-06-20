def my_func(*args):
    my_summ = 0
    for i in inp_str:
        try:
            my_summ += int(i)
        except ValueError:
            print(f"Ошибка! Значение '{i}' не является числом, и в сумме учтено не будет!")
    return my_summ


new_str = 0
while True:
    print("Введите значения, которые нужно сложить, либо 'Q' для выхода")
    inp_str = input(" ").lower()
    inp_q = inp_str.find("q")
    if inp_q > 0:
        break
    inp_str = inp_str.split(" ")
    new_str += my_func(inp_str)
    print(f'Промежуточная сумма равна = {new_str}')

inp_str = inp_str[:inp_q]
inp_str = inp_str.split(" ")
new_str += my_func(inp_str)
print(f'Отлично! Общая сумма равна = {new_str}')
