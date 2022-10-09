# Семинар 5
# 6. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# run-length encoding, RLE) или кодирование повторов — алгоритм сжатия данных,
# заменяющий повторяющиеся символы (серии) на один символ и число его повторов.
# Серией называется последовательность, состоящая из нескольких одинаковых символов.

# сформировать random-текст из некоторого объёма символов
# Записать в первый файл
# Записать после rle в файл
# Из rle распаковать и записать в файл
# попробовать через RegExp (.)\1+

# Очистка консоли
import os
import re
import random


def clear():
    return os.system('cls')


clear()


# создание random-текста random-длины
def get_random_text():
    text = ''
    # количество символов
    for i in range(0, random.randint(5, 20)):
        # количество повторений символов A,B,C,D
        text += chr(random.randint(65, 68)) * random.randint(1, 5)
    return text


# Сжатие данных. На входе текст, на выходе сжатый текст
def compression_data(text):
    # список списков
    comp_list = []
    symbol = text[0]
    count = 1
    for item in text[1:]:
        # если предыдущий символ равен текущему (т.е. повторяется), то инкрементируем счётчик
        if item == symbol:
            count += 1
        else:
            # если не равен, то записываем в список символ и количество повторений из счётчика
            comp_list.append([symbol, count])
            count = 1
            symbol = item
    # записываем послений символ и кол-во его повторений
    comp_list.append([symbol, count])
    # print(comp_list)
    comp_text = ''
    # формируем новый текст по алгоритму RLE
    for item in comp_list:
        if item[1] > 1:
            comp_text += item[0] + str(item[1])
        else:
            comp_text += item[0]
    return comp_text


# Восстановление данных. На входе сжатый RLE текст, на выходе восстановленный текст
def recovery_data(text):
    symbol = text[0]
    symbol_count = ''
    recovery_text = ''
    for item in text[1:]:
        if item.isdigit():
            symbol_count += item
        else:
            if len(symbol_count):
                recovery_text += symbol * int(symbol_count)
                symbol = item
                symbol_count = ''
            else:
                recovery_text += symbol
                symbol = item
    # записываем послений символ согласно кол-ву его повторений
    if len(symbol_count) > 0:
        recovery_text += symbol * int(symbol_count)
    else:
        recovery_text += symbol
    return recovery_text


# Проверка на наличие повторяющихся элементов в тексте.
def check_repeat(text):
    # RegExp. . - любой символ, \1 - тот же текст, что и в первой группе захвата, + - 1 и более повторений
    pattern = r'(.)\1+'
    repeat_list = re.findall(pattern, text)
    # print(type(repeat_list))
    # print(repeat_list)
    # print(len(repeat_list))
    if len(repeat_list):
        return True
    return False


# Запись текста в файл
def write_file(text, file_name):
    with open(file_name, 'w') as data:
        data.write(text)


# Чтение текста из файла
def read_file(file_name):
    with open(file_name, 'r') as data:
        text = data.read()
    print(f'Текст из файла {file_name}: {text}')
    return text


# имена файлов
source_filename = 'source.txt'
compressed_filename = 'compressed.txt'
recovery_filename = 'recovery.txt'

sourse_text = get_random_text()
write_file(sourse_text, source_filename)

text = read_file(source_filename)

repeat = check_repeat(text)

if len(text) == 0:
    print('Файл пустой! Сжимать нечего!')
elif len(text) > 0 and not repeat:
    print(f'В файле {source_filename} нет подряд повторяющихся элементов. Сжатие файла алгоритмом RLE не имеет смысла!')
else:
    text = compression_data(text)
    write_file(text, compressed_filename)

    text = read_file(compressed_filename)

    text = recovery_data(text)
    write_file(text, recovery_filename)

    text = read_file(recovery_filename)

    # проверка
    if sourse_text == text:
        print('Исходный текст равен тексту, полученному из восстановленного файла!')
    else:
        print('Что-то пошло не так!')
