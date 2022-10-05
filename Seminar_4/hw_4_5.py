# Семинар 4
# Очистка консоли
import os
import random


def clear():
    return os.system('cls')


clear()


# 5. Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


# Random-создание многочлена - словаря. Ключи - степени, значения - коэффициенты. На входе степень многочлена.
def get_polinom_dict(k):
    polynom_dict = {}
    # заполняем словарь. Ключ - степень.
    while k != -1:
        coeff = random.randint(-9, 10)
        polynom_dict[k] = coeff
        k -= 1
    return polynom_dict


# Запись многочлена-словаря в файл. На входе словарь и имя файла.
def write_polynom_to_file(polynom_dict, file_name):
    text_string = ''
    # print(polynom_dict.keys())
    max_degree = max(polynom_dict.keys())
    # print(max_degree)
    for degree in range(max_degree, -1, -1):
        # print(polynom_dict[degree])
        if polynom_dict[degree] != 0:
            if polynom_dict[degree] > 0:
                sign = '+'
            else:
                sign = '-'
            # если коэффициент равен единице, то его не пишем
            if abs(polynom_dict[degree]) == 1 and degree != 0:
                temp = ''
            else:
                temp = str(abs(polynom_dict[degree]))
            if degree == 0:
                text_string += sign + ' ' + temp
            elif degree == 1:
                text_string += sign + ' ' + temp + 'x '
            else:
                text_string += sign + ' ' + temp + f'x^{degree} '
    if text_string[-1] == ' ':
        text_string += '= 0'
    else:
        text_string += ' = 0'
    if text_string[0] == '+':
        text_string = text_string[2:]

    # Запись строки в файл
    with open(file_name, 'w') as data:
        data.write(text_string)
    print(f"Random-многочлен: {text_string} записан в файл {file_name}")


# Получение коэффициентов многочлена из строки. На выходе словарь (ключи - степени, значения - коэффициенты)
def get_coeff(polinom_string):
    polinom_dict = {}
    # разбиваем строку. разделитель - пробел
    polinom_list = polinom_string.split(' ')
    sign = 1
    # перебираем каждый элемент списка разделённой строки, не смотрим '= 0'
    for pol_num in range(0, len(polinom_list) - 2):
        # определяем знак коэффициента многочлена
        if polinom_list[pol_num][0] == '-' or polinom_list[pol_num] == '-':
            sign = -1
        # если не знак
        if polinom_list[pol_num] not in ('+', '-'):
            # если нет x (т.е. x^0)
            if polinom_list[pol_num].find('x') == -1:
                polinom_dict[0] = int(polinom_list[pol_num]) * sign
                sign = 1
            # если нет ^ (т.е. x^1)
            elif polinom_list[pol_num].find('^') == -1 and polinom_list[pol_num].find('x') != -1:
                temp = polinom_list[pol_num].replace('x', '')
                if len(temp) == 0:
                    temp = 1
                polinom_dict[1] = int(temp) * sign
                sign = 1
            else:
                # убираем ^
                temp = polinom_list[pol_num].replace('^', '')
                # если перед коэффициентом стоит знак '-', убираем его
                if temp.find('-') != -1:
                    temp = temp.replace('-', '')
                # разбиваем по x, справа степень, слева коэффициент
                temp = temp.split('x')
                if len(temp[0]) == 0:
                    temp[0] = 1
                polinom_dict[int(temp[1])] = int(temp[0]) * sign
                sign = 1
    # print()
    return polinom_dict


# Сложение коэффициентов многочленов (сложение значений одинаковых ключей двух словарей). На выходе словарь-сумма.
def summ_dict(polinom_dict_1, polinom_dict_2):
    summ_dict = polinom_dict_1.copy()
    # обновление словаря (добавление пар ключ-значение из другого словаря)
    summ_dict.update(polinom_dict_2)
    # print(summ_dict)
    # суммирование значений одинаковых ключей двух словарей и запись в новый словарь.
    # если ключа в словаре нет, ошибка не возникает (возвращает 0)
    for summ_keys in summ_dict:
        summ_dict[summ_keys] = polinom_dict_1.get(summ_keys, 0) + polinom_dict_2.get(summ_keys, 0)
    return summ_dict


# Получение многочлена-строки из файла. Возвращает строку-многочлен.
def get_polynom_from_file(file_name):
    with open(file_name, 'r') as data:
        polygon_string = data.read()
    return polygon_string


file_1 = 'file_1.txt'   # файл с первым многочленом
file_2 = 'file_2.txt'   # файл со вторым многочленом
file_3 = 'file_3.txt'   # файл с суммой двух многочленов

k = abs(int(input("Введите натуральную степень k первого многочлена: ")))
polynom_dict = get_polinom_dict(k)
write_polynom_to_file(polynom_dict, file_1)

k = abs(int(input("Введите натуральную степень k второго многочлена: ")))
polynom_dict = get_polinom_dict(k)
write_polynom_to_file(polynom_dict, file_2)

polynom_string_1 = get_polynom_from_file(file_1)
polynom_dict_1 = get_coeff(polynom_string_1)
# print(polynom_dict_1)

polynom_string_2 = get_polynom_from_file(file_2)
polynom_dict_2 = get_coeff(polynom_string_2)
# print(polynom_dict_2)

summ_polynom = summ_dict(polynom_dict_1, polynom_dict_2)
# print(summ_polynom)
print(f'{"=" * 50}')
write_polynom_to_file(summ_polynom, file_3)
