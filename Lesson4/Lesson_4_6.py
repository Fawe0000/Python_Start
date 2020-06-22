"""Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее."""

from itertools import count, cycle
from sys import argv

"""входные параметры скрипта:
skript_name - наименование, 
count_start - начальное значение генератора, 
count_stop - конечное значение генератора, 
cycle_stop - число повторений элементов списка"""

try:
    i = ''
    argum = ''
    count_list = []
    end_list = []
    skript_name, count_start, count_stop, cycle_stop = argv

    # проверяем корректность входных параметров скрипта
    for i, argum in enumerate(argv[1:]):
        argum = int(argum)
        print(f'{i}-й параметр скрипта = {argum}')

    # решаем итератор а)
    for el in count(int(count_start)):
        if el > int(count_stop):
            break
        else:
            count_list.append(el)
    print(count_list)

    # решаем итератор b)
    for i, el in enumerate(cycle(count_list)):
        if i > int(cycle_stop - 1):
            break
        else:
            end_list.append(el)

    print(end_list)

except ValueError:
    print(f'Ошибочное значение "{i}" входного параметра "{argum}"')
