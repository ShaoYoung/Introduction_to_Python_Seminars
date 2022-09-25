# Семинар 1
import random
# Очистка консоли
import os


def clear(): return os.system('cls')


clear()


# 5. Дано число. Проверить кратно ли оно 5 и 10 или 15, но не 30
def multiplicity():
    n = int(input('Введите число '))
    if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and (n % 30 != 0):
        print(f'Число {n} кратно 5 (10, 15) и не кратно 30')
    else:
        print(f'Число {n} НЕ кратно 5 (10, 15) ИЛИ кратно 30')


multiplicity()
