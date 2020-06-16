print("Введите произвольное количество строк, разделенных пробелами:")
text_input = input()
k_word = text_input.count(" ") + 1
print(f"вы ввели {k_word} слов")
len_input = text_input.split(" ")
for i, el in enumerate(len_input):
    print(f"{i}  {el[:10]}")
