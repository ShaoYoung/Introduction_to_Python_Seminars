# Семинар 3
# Очистка консоли
import os


# import random

def clear():
    return os.system('cls')


clear()


# 3. Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


# Вычисление разницы между максимальным и минимальным значением дробной части элементов списка
# на входе string-список
def sub_max_min_float(list_float):
    list_float_part = []
    for item in list_float:
        if '.' in str(item):  # если есть дробная часть, то избавляемся от знака (иначе %1 выдаст некорректный рез-т)
            list_float_part.append(round(abs(item) % 1, 5))  # получаем дробную часть, округляем и добавляем в список
    # print(list_float_part)
    max_value = max(list_float_part)
    print(f'Максимальное значение дробной части {max_value}')
    min_value = min(list_float_part)
    print(f'Минимальное значение дробной части {min_value}')
    result = max_value - min_value
    # # второй вариант (через сортировку списка)
    # list_float_part.sort()
    # result = list_float_part[-1] - list_float_part[0]
    return result


# список задаётся вручную
list_float = [1.1, 1.2, 3.1, 5, -10.01]
print(f'Cписок из вещественных чисел {list_float}')
print(f'Разница между max и min значением дробной части элементов списка {sub_max_min_float(list_float)}')
