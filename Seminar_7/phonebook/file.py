# работа с файлами

import csv
import json
import os
import pickle


# запись файла. на входе справочник (список списков)
def save_txt(phone_book):
    """
    :param phone_book:
    :return: write file
    """
    file_name = 'phone_book.txt'
    book_txt = ''
    for abonent in phone_book:
        ab_record = ' '.join(abonent)
        ab_record += '\n'
        book_txt += ab_record
    with open(file_name, 'w', encoding="utf-8") as file:
        file.write(book_txt)


def save_csv(phone_book):
    """
    :param phone_book:
    :return: write file
    """
    file_name = 'phone_book.csv'
    # открыть cvs-файл для чтения. пустой строки между данными нет.
    with open(file_name, mode='w', encoding='utf-8', newline='') as csvfile:
        # создание объекта writer, delimeter - разделитель
        abonent_writer = csv.writer(csvfile, delimiter=' ')
        # writerow() принимает список, элементы которого будут записаны в строку через символ-разделитель
        for abonent in phone_book:
            abonent_writer.writerow(abonent)


def save_json(phone_book):
    """
    :param phone_book:
    :return: write file
    """
    file_name = 'phone_book.json'
    with open(file_name, mode='w') as jsonfile:
        # преобразовываем объект Python в данные формата JSON и записываем в файл phone_book.json обновлённый справочник
        json.dump(phone_book, jsonfile)


def save_pickle(phone_book):
    """
    :param phone_book:
    :return: write file
    """
    file_name = 'phone_book.data'
    with open(file_name, mode='wb') as file:
        # преобразовываем объект Python в данные формата pickle и записываем в файл phone_book.data
        pickle.dump(phone_book, file)


def save_html(phone_book):
    """
    :param phone_book:
    :return: write file
    """
    file_name = 'phone_book.html'
    # Создание html-файла (строка с полученными данными)
    style = 'style="font-size:30px"'
    book_html = '<html>\n <head></head>\n <body>\n'
    book_html += f'<p {style}><span style="color:blue">Телефонный справочник</span></p>\n'
    book_html += f'<table border="2" bordercolor="red" cellpadding="10" {style}>'
    count = 0
    # заголовки таблицы
    book_html += '<tr><td>№</td><td>Фамилия</td><td>Имя</td><td>Телефон</td><td>Комментарий</td></tr>'
    # записи каждого абонента в соответствующие колонки
    for abonent in phone_book:
        book_html += '<tr>'
        count += 1
        book_html += f'<td>{count}</td>'
        for record in abonent:
            book_html += f'<td>{record}</td>'
        book_html += '</tr>'
    book_html += '</table>'
    book_html += '</body>\n</html>'
    with open(file_name, 'w', encoding="utf-8") as page:
        page.write(book_html)


def read_txt():
    """
    чтение файла в txt-формате. на выходе список строк
    :return: ['','']
    """
    phone_book = []
    file_name = 'phone_book.txt'
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding="utf-8") as file:
            for line in file:
                line = line.rstrip()
                phone_book.append(line)
    return phone_book


def read_csv():
    """
    чтение файла в csv-формате. на выходе список строк
    :return: ['','']
    """
    phone_book = []
    file_name = 'phone_book.csv'
    if os.path.exists(file_name):
        with open(file_name, encoding='utf-8') as csvfile:
            # создаем объект reader, указываем символ-разделитель ","
            book_reader = csv.reader(csvfile, delimiter=" ")
            # построчное считывание из reader. каждая строка объекта - список из строк
            for row in book_reader:
                phone_book.append(' '.join(row))
    return phone_book


def read_json():
    """
    чтение файла в json-формате. на выходе список списков
    :return: [[],[]]
    """
    phone_book = []
    file_name = 'phone_book.json'
    # проверка на наличие файла
    if os.path.exists(file_name):
        with open(file_name, 'r') as jsonfile:
            # Чтение файла phone_book.json и преобразование данных JSON в объект Python
            phone_book = json.load(jsonfile)
    return phone_book


def read_pickle():
    """
    чтение файла в pickle-формате. на выходе список списков
    :return: [[],[]]
    """
    phone_book = []
    file_name = 'phone_book.data'
    # проверка на наличие файла
    if os.path.exists(file_name):
        with open(file_name, 'rb') as file:
            # Чтение файла phone_book.data и преобразование данных pickle в объект Python
            phone_book = pickle.load(file)
    return phone_book


def save_file(phone_book, file_type=4):
    """
    Записывает файл соответствующего типа
    :param file_type: int, номер типа файла
    :param phone_book: [[],[]], телефонная книга
    :return: запись файла
    """
    if file_type == 1:
        save_txt(phone_book)
    if file_type == 2:
        save_csv(phone_book)
    if file_type == 3:
        save_json(phone_book)
    if file_type == 4:
        save_pickle(phone_book)
    if file_type == 5:
        save_html(phone_book)


def read_file(file_type=4):
    """
    чтение из файла. на выходе список списков
    :param file_type: int, номер типа файла
    :return: [[],[]], телефонная книга
    """
    phone_book = []
    if file_type == 1:
        phone_book = read_txt()
    elif file_type == 2:
        phone_book = read_csv()
    elif file_type == 3:
        phone_book = read_json()
    elif file_type == 4:
        phone_book = read_pickle()
    # если список строк, то преобразуем к списку списков
    for i in range(0, len(phone_book)):
        if type(phone_book[i]) == str:
            phone_book[i] = phone_book[i].split()
    return phone_book
