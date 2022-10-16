# Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах.
# под форматами понимаем структуру файлов, например:в файле на одной строке хранится одна часть записи,

# модули:
# main - основной (для запуска БД)
# change_db - внесение изменений в БД
# file - работа с файлами
# tkinter_work - работа в окне Tkinter
# работа с основной БД идёт в pickle-файле
# функционал БД:
# просмотр абонентов
# поиск абонента
# добавление абонента
# удаление абонента
# сохранение БД в txt, csv, json

# закомментированный код остался от предыдущей версии БД, работающей в терминале

# import os
# import user_input as ui
# import change_db as chdb
# import file as f
import tkinter_work as tkw


# Очистка консоли
# def clear():
#     return os.system('cls')
#
#
# clear()

tkw.start()

# # выбор действия пользователем
# file_type = ui.get_type()
# action = ui.get_action()
# # просмотр справочника
# if action == 1:
#     phone_book = f.read_file(file_type)
#     ui.print_phonebook(phone_book)
# # поиск информации в справочнике
# elif action == 2:
#     finded_abonent = chdb.find_in_file(file_type)
#     ui.print_phonebook(finded_abonent)
# # добавление нового элемента в справочник
# elif action == 3:
#     chdb.add_abonent(file_type)
# # удаление информации из справочника
# elif action == 4:
#     chdb.remove_element(file_type)
# # изменение информации в справочнике
# elif action == 5:
#     chdb.change_abonent(file_type)



