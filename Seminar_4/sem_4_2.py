# Семинар 4
# Очистка консоли
import os
import math


def clear():
    return os.system('cls')


clear()

# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения;
# 2) с помощью дополнительных библиотек Python.

coeff = input("Введите коэффициенты квадратного уравнения (A, B, C через пробел): ")
coeff = coeff.split(' ')
coeff = list(map(int, coeff))
a, b, c = coeff
print(a, b, c)
# Дискриминант
# D = b^2 − 4ac
x = []
d = b ** 2 - 4 * a * c
if d < 0:
    print('В этом уравнении корней нет!')
elif d == 0:
    x.append(-b / (2 * a))
else:
    x.append((-b + math.sqrt(d)) / (2 * a))
    x.append((-b - math.sqrt(d)) / (2 * a))
print(f'Корни этого квадратного уравнения {x}')

# Изучить встроенные возможности Python
