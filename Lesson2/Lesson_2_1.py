test_string = "это строка"
test_list = list("это список")
test_tuple = tuple("это кортеж")
test_set = frozenset("это множество")
test_dict = dict(zip(test_tuple,test_list))
work_list = [1, 2.3, 3+5j, test_string,test_list, True, None, test_tuple, test_set, test_dict]
print('Типы данных в строке "work_list"')
for ind, ty in enumerate(work_list):
    print(f'{ind}) значение "{work_list[ind]}" имеет тип данных {type(ty)}')
