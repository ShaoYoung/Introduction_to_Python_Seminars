# Семинар 1
import random
# Очистка консоли
import os
def clear(): return os.system('cls')
clear()

# 4. Показать первую цифру дробной части числа
def first_float():
    n = input("Введите вещественное число ")
    n_list = n.split('.')
    print(n_list)
    print(n_list[1][0])

first_float()