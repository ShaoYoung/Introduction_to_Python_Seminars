# Семинар 3
# Очистка консоли
import os
import random


def clear():
    return os.system('cls')


clear()


# 1. Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# Задание списка из n случайных чисел
def get_list(n):
    list_random = []
    for i in range(1, n + 1):
        list_random.append(random.randint(0, 9))
    return list_random


# Вычисление суммы элементов списка, стоящих на нечётной позиции
def find_summ_odd(list_random):
    summ = 0
    for i in range(1, len(list_random), 2):
        summ += list_random[i]
    return summ


n = 5  # длина списка
list_random = get_list(n)
print(list_random)
print(f'Сумма элементов списка, стоящих на нечётных позициях = {find_summ_odd(list_random)}')
