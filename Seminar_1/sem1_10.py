# Семинар 1
import random
from math import sqrt
# Очистка консоли
import os
def clear(): return os.system('cls')
clear()

# 10. Найти расстояние между двумя точками пространства
# 5. Домашнее задание

# Вычисдение расстояния между двумя точами в 2D пространстве. На входе два списка с координатами X и Y
def find_distance(a_list, b_list):
    # первый вариант. через библиотеку math (нагляднее)
    distance = round(sqrt((a_list[0] - b_list[0]) ** 2 + (a_list[1] - b_list[1]) ** 2), 2)
    # второй варинат. через возведение в степень 0.5 (быстрее и не надо подключать библиотеку math)
    # distance = round(((a_list[0] - b_list[0]) ** 2 + (a_list[1] - b_list[1]) ** 2) ** 0.5, 2)
    return distance

# Ввод координат. На входе литера точки, на выходе список с координатами X и Y
def input_coord(letter):
    correct_input = False
    while not correct_input:
        point = input(f"Введите координаты точки {letter} (целые числа через запятую) ")
        point_list = point.split(',')
        if (not point_list[0].isdigit()) or (not point_list[1].isdigit()):
            print("Некорректный ввод")
        else:
            correct_input = True
    point_list[0] = int(point_list[0])
    point_list[1] = int(point_list[1])
    return point_list


a_list = input_coord("A")
b_list = input_coord("B")
print(f"Растояние между точками = {find_distance(a_list, b_list)}")

