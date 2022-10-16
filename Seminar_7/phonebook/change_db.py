# изменения в базе данных (добавление, поиск, удаление, замена)

import file as f


def add_abonent(file_type):
    """
    добавление абонента
    :param file_type:
    :return: save new abonent in file
    """
    new_abonent = []
    new_abonent.append(input('Введите фамилию абонента: '))
    new_abonent.append(input('Введите имя абонента: '))
    new_abonent.append(input('Введите телефон абонента: '))
    new_abonent.append(input('Введите описание абонента: '))
    phone_book = f.read_file(file_type)
    phone_book.append(new_abonent)
    f.save_file(file_type, phone_book)


def find_in_file(find_text):
    """
    поиск в файле. ищет в справочнике, полученном из файла, возвращает список найденных элементов
    :param file_type:
    :return: [[],[]]
    """
    # search_info = input('Введите элемент (текстом): ').lower()
    search_info = find_text.lower()
    phone_book = f.read_file()
    finded_info = []
    # если в элементе справочника есть искомая строка, записываем его в список найденных элементов
    for element in phone_book:
        if search_info in ''.join(element).lower():
            finded_info.append(element)
    return finded_info


def remove_element(del_info):
    """
    удаление информации из справочника
    :param file_type:
    :return:перезапись телефонной книги без удалённого абонента
    """
    remove_info = find_in_file(del_info)
    if len(remove_info) == 0:
        # print(f'Не могу удалить {len(remove_info)} абонента(ов)! ')
        return False
    else:
        new_phone_book = []
        phone_book = f.read_file()
        # ищем вхождение по каждому абоненту
        for element in phone_book:
            add = True
            if element[0] == remove_info[0][0] and element[1] == remove_info[0][1] and element[2] == remove_info[0][
                2] and element[3] == remove_info[0][3]:
                add = False
            if add:
                new_phone_book.append(element)
        f.save_file(new_phone_book)
        return True
