# Семинар 4
# Очистка консоли
import os
import math


def clear():
    return os.system('cls')


clear()


# 1. Вычислить число c заданной точностью d
# 	Пример:
# 	при d = 0.001, π = 3.141        10-1 <= d <= 10-10

# 1. через строку, потом длина дробной части, потом round
# 2. через log ( 1 / d )

# Отображение числа π с необходимой точностью
def print_accuracy(d):
    if d.find('.') != -1:
        accuracy = d.split('.')
        accuracy = len(accuracy[1])
    elif d.find(',') != -1:
        accuracy = d.split(',')
        accuracy = len(accuracy[1])
    else:
        accuracy = 0
    print(f'Первый вариант. Число π с точностью {d} = {round(math.pi, accuracy)}')
    # Второй вариант (через десятичный логарифм)
    if d.find(',') != -1:
        d = d.replace(',', '.', 1)
    if float(d) != 0:
        accuracy = int(math.log10(1 / float(d)))
    else:
        accuracy = 0
    print(f'Второй вариант. Число π с точностью {d} = {round(math.pi, accuracy)}')


d = input('Введите число d (10-1 <= d <= 10-10): ')
print(d)
print_accuracy(d)
