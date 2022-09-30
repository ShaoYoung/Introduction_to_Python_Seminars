# Семинар 3
# Очистка консоли
import os
import time
import math


def clear():
    return os.system('cls')


clear()


# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
# время, выраженное в секундах с начала эпохи Unix 01.01.1970 г.
# x = time.time()
# print(x)
# # time.sleep(1.5)     #задержка (в секундах)
# x = time.time_ns()  # то же, только в наносекундах
# print(x)
# x = int(x % 10000 / 100)
# print(x)


# функция получения псевдослучайного числа без использования random
def random_in_time(a, b):
    random_ok = False
    while not random_ok:
        x = time.time_ns()  # время в наносекундах
        x = int(x // 100)  # убираем два лишних нуля
        x = x % b  # максимальное random-число
        time.sleep(0.001)  # задержка для получения другого совсем произвольного time.time_ns
        y = time.time_ns()
        y = int(y // 100)  # убираем два лишних нуля
        if a > 0:
            y = y % a  # минимальное random-число
        else:
            y = 0
        random_number = x - y
        if a <= random_number <= b:
            random_ok = True
    print(f'Случайное число в диапазоне от [{a} до {b}) -> {random_number}')


# функция получения псевдослучайного числа без использования random (через пропорцию)
def random_proportion(a, b):
    x = time.time_ns()  # время в наносекундах
    x = int(x // 100)  # убираем два лишних нуля
    x = x % b
    random_number = int(a + (b - a) * x / b)
    print(f'Случайное число в диапазоне от [{a} до {b}) -> {random_number}')


a = 1999990  # начало random-диапазона [a
b = 2000000  # конец random-диапазона b)
# random_in_time(a, b)
random_proportion(a, b)
