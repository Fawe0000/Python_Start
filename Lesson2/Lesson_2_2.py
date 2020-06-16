print("Задаем список")
l_list = int(input(" Введите количество необходимых элементов списка "))
input_list = []
for i in range(l_list):
    val = input(f"введите {i+1}-й элемент списка: ")
    input_list.append(val)
print(f' Введен список: {input_list}')
for el in range(0, l_list//2*2, 2):
    input_list[el], input_list[el+1] = input_list[el+1], input_list[el]
print(f' Попарно перевернутый список:  {input_list}')
