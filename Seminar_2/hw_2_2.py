# Семинар 2
# Очистка консоли
import os


def clear():
    return os.system('cls')


clear()


# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# 2. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ]

def mult_numbers(n):
    mult = []
    if n < 1:
        print("Некорректный ввод!")
    for i in range(1, n + 1):
        temp = 1
        for j in range(1, i + 1):
            temp *= j
        mult.append(temp)
    return mult


n = int(input("Введите число N "))
print(f"Для числа {n} набор произведений чисел от 1 до {n} следующий {mult_numbers(n)}")
