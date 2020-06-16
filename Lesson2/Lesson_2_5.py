start_list = [8, 7, 5, 3, 3, 2]
print(f"В настоящий момент рейтинг такой: {start_list}")
new_n = int(input("Введите новое значение: "))
end_list = []
for enum, el in enumerate(start_list):
    print(enum, el, new_n)
    if new_n > el:

        print(end_list.insert(enum, new_n))
        print(f"if {end_list}")
    else:
        end_list.insert(enum, el)
        print(f"else {end_list}")

print(end_list)
