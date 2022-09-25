# Семинар 1
import random
# Очистка консоли
import os


def clear(): return os.system('cls')


clear()


# 6. Дано число обозначающее день недели. Вывести его название и указать является ли он выходным
# 1. Домашнее задание
def check_day_of_week(day):
    text = ""
    if day == 1:
        text = "Понедельник"
    elif day == 2:
        text = "Вторник"
    elif day == 3:
        text = "Среда"
    elif day == 4:
        text = "Четверг"
    elif day == 5:
        text = "Пятница"
    elif day == 6:
        text = "Суббота"
    elif day == 7:
        text = "Воскресенье"
    else:
        text = "Некорректный ввод!"
    if day in (6, 7):
        text += " Это выходной день"
    if day in range(1, 6):
        text += " Это рабочий день"
    return text


day = int(input("Введите порядковый номер дня недели "))
print(check_day_of_week(day))
