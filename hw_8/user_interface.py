# модуль интерфейса

import check

def start():
    greetings = 'Привет! Это твоя телефонная книга.'
    print(f'{greetings}\n')


def menu():
    what_to_do = 'Что будем делать? Выберите соответствующую цифру в меню:'
    import_data = '1. импорт'
    export_data = '2. экспорт'
    search_data = '3. поиск'
    print_data = '4. печать'
    print(f'{what_to_do}\n\n{import_data}\n{export_data}\n{search_data}\n{print_data}\n')
    return check.digit_check()