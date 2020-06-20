"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
 имя, фамилия, год рождения, город проживания, email, телефон.
 Функция должна принимать параметры как именованные аргументы.
 Реализовать вывод данных о пользователе одной строкой."""

print("Функция, принимающая и описывающая данные пользователя")


def string_func(name_i, surname_i, birth_year_i, sity_i, email_i, phone_i):
    str_i = str("Имя: " + name_i +
                ", Фамилия: " + surname_i +
                ", Год рождения: " + birth_year_i +
                ", Город проживания: " + sity_i +
                ", e-mail: " + email_i +
                ", телефон: " + phone_i)
    print("* " * 60)
    print(str_i)
    print("* " * 60)
    pass


i_surname = input("Введите фамилию: ").title()
i_name = input("Введите имя: ").title()
i_sec_name = input("Введите отчество: ").title()
i_birth_year = input("Введите год рождения: ")
i_sity = input("Введите город проживания: ").title()
i_email = input("Введите e-mail: ")
i_phone = input("Введите номер телефона: ")

string_func(name_i=i_name, surname_i=i_surname, birth_year_i=i_birth_year, sity_i=i_sity, email_i=i_email,
            phone_i=i_phone)
