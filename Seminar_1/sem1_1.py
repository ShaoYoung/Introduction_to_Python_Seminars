# Семинар 1
import random
# Очистка консоли
import os


def clear(): return os.system('cls')


clear()


# 1. По двум заданным числам проверить является ли одно квадратом второго.
def check_square():
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    # print (a ** 2)
    # print (b ** 2)
    if a == b ** 2 or b == a ** 2:
        print("Да, одно число является квадратом другого")
    else:
        print("Нет, одно число НЕ является квадратом другого")


check_square()
