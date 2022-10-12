# Семинар 4
# Очистка консоли
import os
import random


def clear():
    return os.system('cls')


clear()


# 4. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и
# записать в файл многочлен степени k.
# 	Пример:
# 	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# Random-создание многочлена - словаря. Ключи - степени, значения - коэффициенты. На входе степень многочлена.
def get_polinom_dict(k):
    polynom_dict = {}
    # заполняем словарь. Ключ - степень.
    while k != -1:
        coeff = random.randint(0, 101)
        polynom_dict[k] = coeff
        k -= 1
    return polynom_dict

# REFACTORING
# Random-создание многочлена - словаря. Ключи - степени, значения - коэффициенты. На входе степень многочлена.
# Заполнение через Dict comprehension
def get_polinom_dict_2(k):
    # заполняем словарь. Ключ - степень.
    polynom_dict = {i: random.randint(0, 101) for i in range(k, -1, -1)}
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


k = abs(int(input("Введите натуральную степень k: ")))
polynom_dict = get_polinom_dict(k)
print(f'Словарь-полином: {polynom_dict}')

# REFACTORING
polynom_dict = get_polinom_dict_2(k)
print(f'Словарь-полином (через Dict comprehension): {polynom_dict}')

file_name = 'file.txt'
write_polynom_to_file(polynom_dict, file_name)

# степень через ^ или **
