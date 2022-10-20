# Обработка событий от пользователя, изменение модели

import model as mod
import view_terminal as vt
import json
# для нахождения среднего значения
from statistics import mean


# начало работы controller, инициализация БД
def start_work():
    file_name = 'Data_base.db'
    mod.init_db(file_name)


# просмотр БД
def preview_base():
    info = mod.get_info('SELECT * FROM personal')
    vt.print_db(info)


# просмотр БД_tk
def preview_base_tk():
    info = mod.get_info('SELECT * FROM personal')
    return info


# добавление информации в БД_tk
def add_db_tk(worker):
    # получаем новую запись БД
    # worker = list(vt.get_data('нового').values())
    # print(worker)
    mod.add_record('INSERT INTO personal VALUES(?, ?, ?, ?, ?, ?);', worker)


# добавление информации в БД
def add_db():
    # получаем новую запись БД
    worker = list(vt.get_data('нового').values())
    # print(worker)
    mod.add_record('INSERT INTO personal VALUES(?, ?, ?, ?, ?, ?);', worker)


# поиск информации в БД
def find_info():
    print('Буду искать информацию. Заполните одно поле БД. Ищу по первому совпадению!')
    worker = vt.get_data('искомого')
    # print(worker)
    # ищем первый столбец, в какое поле БД пользователь ввёл данные
    for key in worker:
        if worker[key] != '' and worker[key] != None:
            column = key
            value = worker[key]
            info = mod.find_record(f'SELECT * FROM personal WHERE "{column}" LIKE "{value}"')  # LIKE - поиск по шаблону
            break
            # print(column, value)
            # print(type(column), type(value))
    print('Нашёл:')
    # показываем найденную запись
    if not len(info):
        print('Запрашиваемой информации нет в БД!')
        return []
    else:
        vt.print_db(info)
        return [column, value]


# поиск информации в БД_tk
def find_info_tk(worker):
    # print('Буду искать информацию. Заполните одно поле БД. Ищу по первому совпадению!')
    # worker = vt.get_data('искомого')
    # print(worker)
    # ищем первый столбец, в какое поле БД пользователь ввёл данные
    info = []
    for key in worker:
        if worker[key] != '' and worker[key] != None:
            column = key
            value = worker[key]
            info = mod.find_record(f'SELECT * FROM personal WHERE "{column}" LIKE "{value}"')  # LIKE - поиск по шаблону
            break
            # print(column, value)
            # print(type(column), type(value))
    # print('Нашёл:')
    # показываем найденную запись
    if not len(info):
        # print('Запрашиваемой информации нет в БД!')
        return []
    else:
        # vt.print_db(info)
        # return [column, value]
        return [info, column, value]


# удаление информации из БД
def del_info():
    # ищем запись БД
    info = find_info()
    # если есть записи БД
    if len(info):
        # контрольный вопрос для подтверждения удаления записи
        accept_delete = input('Удаляем? 1 - Да, 0 - Нет: --> ')
        # print(type(info[0]), '-', type(info[1]))
        # print(info[0], '-', info[1])
        if int(accept_delete):
            mod.modify_record(f'DELETE FROM personal WHERE "{info[0]}" = "{info[1]}"')


# удаление информации из БД_tk
def del_info_tk(worker):
    # ищем запись БД
    info = find_info_tk(worker)
    # если есть записи БД
    if len(info):
        info = [info[1], info[2]]
        # контрольный вопрос для подтверждения удаления записи
        # accept_delete = input('Удаляем? 1 - Да, 0 - Нет: --> ')
        # # print(type(info[0]), '-', type(info[1]))
        # # print(info[0], '-', info[1])
        # if int(accept_delete):
        mod.modify_record(f'DELETE FROM personal WHERE "{info[0]}" = "{info[1]}"')


# изменение информации в БД
def modify_info():
    info = find_info()
    # если есть записи БД
    if len(info):
        # запрос обновлённых полей БД
        new_data = vt.get_data('(обновлённые)')
        # меняем те поля, где есть не пустой ввод
        for key in new_data:
            if new_data[key] != '':
                mod.modify_record(f'UPDATE personal SET "{key}" = "{new_data[key]}" WHERE "{info[0]}" = "{info[1]}"')


# статистика
def stat():
    correct = lambda x: int(x) if x.isdigit() and 1 <= int(x) <= 4 else None
    print('Могу посчитать:')
    while True:
        stat_action = correct(input(
            '1 - количество записей в БД\n2 - минимальное значение\n3 - максимальное значение\n4 - среднее значение\n-->> '))
        if stat_action in range(1, 5):
            break
    while True:
        print('Введите цифру 1 в одном поле БД, из которого вы хотите получить информацию: ')
        stat_column = vt.get_data('для сбора статистической информации')
        count = 0
        for key in stat_column:
            if stat_column[key] != '' and stat_column[key] != None:
                column = key
                value = stat_column[key]
                count += 1
        if count == 1:
            break
        print('Не корректный ввод!')
    # print(count, column, value)

    # получаем список единичных кортежей по выбранному столбцу
    info = mod.get_info(f'SELECT "{column}" FROM personal')
    # print(info)
    list_data = []
    # собираем список значений по выбранному столбцу БД
    for item in info:
        list_data.append(item[0])
    # print(list_data)
    if stat_action == 2 and column in ['salary', 'bonus']:
        print(f'Все значения по полю БД {column} {list_data}. Минимальное значение {min(list_data)}.')
    elif stat_action == 3 and column in ['salary', 'bonus']:
        print(f'Все значения по полю БД {column} {list_data}. Максимальное значение {max(list_data)}.')
    elif stat_action == 4 and column in ['salary', 'bonus']:
        print(f'Все значения по полю БД {column} - {list_data}. Среднее значение {round(mean(list_data), 2)}.')
    else:
        find_value = input(f'Введите значение, количество вхождений в {column} которого вы хотите узнать ')
        if find_value.isdigit():
            find_value = int(find_value)
        # считаем количество вхождений в поле БД
        count_entry_info = list_data.count(find_value)
        print(f'Количество вхождений {find_value} в {column} - {count_entry_info}')


# выгрузка БД в json-файл
def save_json():
    """
    :param: В будущем можно выгружать любую выборку из БД
    :return: write file
    """
    # получаем всю БД
    info = mod.get_info('SELECT * FROM personal')
    # делаем из списка словарь (key - номер записи работника, value - данные из БД)
    worker_json = {}
    for count in range(1, len(info) + 1):
        worker_json[count] = info[count - 1]
    print(f'В файл будет записан следующий словарь: {worker_json}')
    file_name = 'db.json'
    with open(file_name, mode='w') as jsonfile:
        # преобразовываем объект Python в данные формата JSON и записываем в файл phone_book.json обновлённый справочник
        json.dump(worker_json, jsonfile)
