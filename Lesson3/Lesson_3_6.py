"""Реализовать функцию int_func(), принимающую слово из маленьких латинских букв
и возвращающую его же, но с прописной первой буквой. """


def int_func(inp_str):
    inp_list = list(inp_str)
    for i in inp_list:
        if 122 < ord(i) or ord(i) < 97:
            exp_str = 'ОШИБКА! Слово "' + inp_str + '" содержит символы кроме маленьких латинских букв'
            return 0, exp_str
    exp_str = inp_str.title() + " "
    return 1, exp_str


""" В программу должна попадать строка из слов, разделенных пробелом. 
Каждое слово состоит из латинских букв в нижнем регистре. 
Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы."""

while True:
    print("Введите строку из слов, разделенных пробелом? или '0' для выхода")
    inp_str = input(" ")
    inp_null = inp_str.find("0")
    if inp_null >= 0:
        break
    inp_str = inp_str.split(" ")
    p_res = ''
    res_str = ''
    for i in inp_str:
        p_res = int_func(i)
        if p_res[0]:
            res_str += p_res[1]
        else:
            print(p_res[1])

print(f'\n Итоговая строка: \n {"----" * 20} \n "{res_str}" \n {"----" * 20} \n')
