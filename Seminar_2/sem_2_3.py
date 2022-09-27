# Семинар 2
# Очистка консоли
import os


def clear():
    return os.system('cls')


clear()

# 3.Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой

# print(chr(1108))
# print(ord("q"))
# print(ord("й"))
import random

first_string = ""
for i in range(50):
    first_string += chr(random.randint(1070, 1100))
print(first_string)
# first_string = input("Введите первую строку: ")
second_string = input("Введите вторую строку: ")
result = first_string.count(second_string)
print(f"Количество вхождений второй строки в первую {result}")
