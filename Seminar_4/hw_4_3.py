# Семинар 4
# Очистка консоли
import os


def clear():
    return os.system('cls')


clear()


# 3. Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# Исключение повторяющихся элементов исходной последовательности (через множество)
def set_change(list_number):
    # Преобразуем в множество. Повторяющиеся элементы игнорируются.
    set_number = set(list_number)
    # print(f'Множество {set_number}')
    # Преобразуем в список, т.к. по условию задачи выводить надо список
    list_number = list(set_number)
    print(f'Список элементов (повторяющиеся элементы исключены): {list_number}')


# Поиск неповторяющихся элементов исходной последовательности
def non_repeat(list_number):
    non_repeat_list = []
    for elem in list_number:
        if list_number.count(elem) == 1:
            non_repeat_list.append(elem)
    print(f'Список неповторяющихся элементов исходной последовательности {non_repeat_list}')


order = input('Введите последовательность чисел (в качестве символа-разделителя используйте пробел: ')
list_number = order.split(' ')
set_change(list_number)
non_repeat(list_number)

# Преобразуем список строк в список int
# Функция map применяет функцию int к каждому элементу объекта list_number,
# потом результат преобразовывается в список.
# list_number = list(map(int, list_number))
# list_number.sort()
# print(f'Сортированный int-список {list_number}')
