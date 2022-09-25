# Семинар 1
import random
# Очистка консоли
import os
def clear(): return os.system('cls')
clear()

# 3. Вывести на экран числа от -N до N
def print_numbers():
    n = int(input("Введите число N "))
    result = ""
    for i in range(-n, n+1):
        result += str(i)
        result += ", "
    print(result[0:(len(result)-2)])

print_numbers()