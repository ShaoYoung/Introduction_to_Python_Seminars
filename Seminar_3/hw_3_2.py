# Семинар 3
# Очистка консоли
import os
import random


def clear():
    return os.system('cls')


clear()


# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Задание списка из n случайных чисел
def get_list(n):
    list_random = []
    for i in range(1, n + 1):
        list_random.append(random.randint(0, 9))
    return list_random


# Нахождение произведений пар чисел списка
def pair_miltiply(list_random):
    list_multiply = []
    for i in range(0, len(list_random) // 2):
        # перемножаем элементы сначала и с конца списка и добавляем в новый список
        list_multiply.append(list_random[i] * list_random[-i - 1])
    # если количество элементов списка нечетное, то добавляем средний элемент списка в квадрате
    if len(list_random) % 2:
        # if len(list_random) % 2 == 1:     #другой вариант проверки на нечётность
        list_multiply.append(list_random[(len(list_random) // 2)] ** 2)
    return list_multiply


n = int(input('Введите длину списка '))  # длина списка
list_random = get_list(n)
print(f'Список {list_random}')
print(f'Произведение пар чисел списка {pair_miltiply(list_random)}')
