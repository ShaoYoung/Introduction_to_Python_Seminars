# Семинар 4
# Очистка консоли
import os
import sys


def clear():
    return os.system('cls')


clear()


# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.


def find_max(list_number):
    max_number = -sys.maxsize
    for number in list_number:
        if number.isdigit():
            if int(number) > max_number:
                max_number = int(number)
    # второй вариант (нет проверки на цифры)
    max_number = max(list_number)
    return max_number


def find_min(list_number):
    min_number = sys.maxsize
    for number in list_number:
        if number.isdigit():
            if int(number) < min_number:
                min_number = int(number)
    # второй вариант (нет проверки на цифры)
    min_number = min(list_number)
    return min_number


string_number = input('Введите строку из чисел. В качестве символа-разделителя используйте пробел. ')
list_number = string_number.split(' ')
print(f'Список чисел: {list_number}')
print(f'Максимальное число {find_max(list_number)}')
print(f'Минимальное число {find_min(list_number)}')
