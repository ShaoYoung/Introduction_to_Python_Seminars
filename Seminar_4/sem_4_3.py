# Семинар 4
# Очистка консоли
import os


def clear():
    return os.system('cls')


clear()


# 3. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное)
# этих двух чисел.

# Наибольший общий делитель
def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)

# Наименьшее общее кратное
def nok(a, b):
    return int(abs(a * b) / nod(a, b))


x = 11
y = 17
print(f'Наибольший общий делитель {nod(x, y)}')
print(nok(x, y))
