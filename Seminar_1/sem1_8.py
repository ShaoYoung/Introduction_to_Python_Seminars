# Семинар 1
import random
# Очистка консоли
import os


def clear(): return os.system('cls')


clear()


# 8. Сообщить в какой четверти координатной плоскости или на какой оси находится точка с координатами Х и У.
# 3. Домашнее задание
def quarter(x, y):
    text = None
    if x > 0 and y > 0:
        text = "Первая четверть"
    elif x > 0 and y < 0:
        text = "Вторая четверть"
    elif x < 0 and y < 0:
        text = "Третья четверть"
    elif x < 0 and y > 0:
        text = "Четвёртая четверть"
    elif x == 0 and y == 0:
        text = "Пересечение координатных осей"
    elif x == 0 and y != 0:
        text = "Ось X"
    elif x != 0 and y == 0:
        text = "Ось Y"
    return text


x = int(input("Введите x "))
y = int(input("Введите y "))
print(quarter(x, y))
