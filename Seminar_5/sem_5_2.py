# Семинар 5
# 2. Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую
# последовательность. Порядок элементов менять нельзя.
# Пример:
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

# Очистка консоли
import os
import random


def clear():
    return os.system('cls')


clear()


# Поиск возрастающих последовательностей (по всей длине списка)
def find_increasing_successions(list_numbers):
    increasing_successions = []
    for i in range(0, len(list_numbers)):
        temp = list_numbers[i]
        temp_list = [list_numbers[i]]
        for j in range(i, len(list_numbers)):
            if list_numbers[j] > temp:
                temp_list.append(list_numbers[j])
                temp = list_numbers[j]
        if len(temp_list) > 1:
            increasing_successions.append(temp_list)
    return increasing_successions


# задание списка случайных чисел (от 1 до 10) случайной длины (от 1 до 10) через List comprehension
list_numbers = [random.randint(1, 10) for i in range(1, random.randint(5, 11))]
print(f'Список случайных чисел: {list_numbers}')
print(f'Список возрастающих последовательностей: {find_increasing_successions(list_numbers)}')
