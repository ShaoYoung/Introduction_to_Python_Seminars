# Пользовательский интерфейс


def get_action():
    """
    Ввод действия
    :return: int, номер выбора (1-5)
    """
    correct_input = False
    while not correct_input:
        action = input(
            'Пожалуйста, выберите действие:\n 1 - Просмотр справочника\n 2 - Поиск абонента\n 3 - Добавление абонента\n 4 - Удаление абонента\n 5 - Изменение записи\n -> ')
        if not action.isdigit() or len(action) != 1 or not 1 <= int(action) <= 5:
            print('Некорректный ввод! Попробуйте ещё раз.')
        else:
            correct_input = True
    return int(action)


def get_type():
    """
    Ввод типа файла, с которым будет работать пользователь
    :return: int, номер типа файла (1-4)
    """
    print('\033[1m\033[31mТелефонный справочник.\033[0m')
    correct_input = False
    while not correct_input:
        action = input('Пожалуйста, выберите тип файла БД:\n 1 - txt\n 2 - csv\n 3 - json\n 4 - pickle\n -> ')
        if not action.isdigit() or len(action) != 1 or not 1 <= int(action) <= 4:
            print('Некорректный ввод! Попробуйте ещё раз.')
        else:
            correct_input = True
    return int(action)
    # return 1


def print_phonebook(phone_book):
    """
    печатает телефонную книгу (элемент книги)
    :param phone_book: list
    :return: print
    """
    if len(phone_book):
        for element in phone_book:
            for item in element:
                print(f'{item} ', end='')
            print()
    else:
        print('Ничего не найдено!')
