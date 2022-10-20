# Работа с пользователем в терминале (ввод и отображение информации)
import controller as cont


# выбор действия пользователя БД
def input_action():
    while True:
        user_choice = input('1 - просмотреть базу\n2 - добавить запись\n3 - найти сотрудника\n4 - удалить запись'
                            '\n5 - изменение данных\n6 - статистика\n7 - выгрузка БД в json-файл\nq - выход \n-->> ')
        if user_choice == '1':
            cont.preview_base()
        elif user_choice == '2':
            cont.add_db()
        elif user_choice == '3':
            cont.find_info()
        elif user_choice == '4':
            cont.del_info()
        elif user_choice == '5':
            cont.modify_info()
        elif user_choice == '6':
            cont.stat()
        elif user_choice == '7':
            cont.save_json()
        elif user_choice == 'q':
            print('Завершение работы')
            break
        else:
            print('Не верно введён режим работы!')


# печать БД. на входе список кортежей
def print_db(db):
    for worker in db:
        print(*worker)


# получение информации от пользователя
def get_data(text):
    # пустой список worker = [None for i in range(0, 6)], словарь лучше
    print(f'Введите данные {text} работника: ')
    # проверка корректности ввода и преобразование в int (salary и bonus)
    correct = lambda x: int(x) if x.isdigit() and int(x) >= 0 else None
    worker = {
        'surname': input('Фамилия: '),
        'name': input('Имя: '),
        'gender': input('Пол: '),
        'position': input('Должность: '),
        # проверяем введённые данные и, если всё верно, преобразуем в INT, т.к. поле БД INT
        'salary': correct(input('Зарплата: ')),
        'bonus': correct(input('Премия: '))
    }
    return worker
