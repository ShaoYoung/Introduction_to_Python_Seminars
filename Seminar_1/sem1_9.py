# Семинар 1
import random
# Очистка консоли
import os


def clear(): return os.system('cls')


clear()


# 9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат
# для точек этой четверти
# 4. Домашнее задание
def possible(quarter):
    text = "Допустимые значения координат для этой черверти: "
    if quarter == 1:
        text += "x > 0, y > 0"
    elif quarter == 2:
        text += "x < 0, y > 0"
    elif quarter == 3:
        text += "x < 0, y < 0"
    elif quarter == 4:
        text += "x > 0, y < 0"
    return text


quarter = int(input("Введите номер четверти "))
if 1 <= quarter <= 4:
    print(possible(quarter))
else:
    print("Некорректный ввод!")
