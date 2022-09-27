# Семинар 2
# Очистка консоли
import os


def clear():
    return os.system('cls')


clear()

# 1.Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#     Пример:
#     - Для N = 5: 1, -3, 9, -27, 81

n = int(input("Введите натуральное число n "))
result = "1, "
# sign = 1
res = 1
for i in range(1, n):
    # result += str(i * (-3) )
    # result += str(3 ** i * sign)
    res *= (-3)
    result += str(res)
    result += ", "
    # result += ", "
    # sign = -sign
print(result[0:(len(result) - 2)])
