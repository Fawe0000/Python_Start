start_list = [8, 7, 5, 3, 3, 2]
print(f"В настоящий момент рейтинг такой: {start_list}")
new_n = int(input("Введите новое значение: "))
start_list.append(new_n)
start_list = sorted(start_list, reverse=True)
print(f"Рейтинг, включая введенное значение: {start_list}")