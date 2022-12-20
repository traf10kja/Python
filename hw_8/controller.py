import import_data as id
import export_data as ed
import print_data as pd
import search_data as sd
import user_interface as ui


def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    brith_name = input("Введите дату рождения: ")
    phone_number = input("Введите номер контакта: ")
    note = input("Введите категорию контакта: ")
    return [last_name, first_name, middle_name, brith_name, phone_number, note]

def choice_sep():
    sep = input("Введите разделитель: ")
    if sep == "":
        sep = None
    return sep

def user_choice():

    choice_num = ui.menu()
    if choice_num < 0 or choice_num > 7:
        print('\nОшибка ввода!\n\nЧисло должно соответствовать пункту меню!\n')
        user_choice()
    elif choice_num == 1:
        id.import_data()
    elif choice_num == 2:
        ed.export_data()
    elif choice_num == 3:
        word = input("Введите данные для поиска: ")
        data = ed()
        item = sd(word, data)
        if item != None:
            print("Фамилия".center(20), "Имя".center(20), "Отчество".center(20), "Дата рождения".center(20), "Телефон".center(15), "Категория".center(30))
            print("-"*130)
            print(item[0].center(20), item[1].center(20), item[2].center(20), item[3].center(20), item[4].center(15), item[5].center(30))
        else:
            print("Данные не обнаружены")
    elif choice_num == 4:
        pd.print_data()