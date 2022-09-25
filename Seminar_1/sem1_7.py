# Семинар 1
import random
# Очистка консоли
import os


def clear(): return os.system('cls')


clear()


# 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат. not (X or Y or Z) = not X and not Y and not Z
# 2. Домашнее задание
def logical(x, y, z):
    left = not (x or y or z)
    right = not x and not y and not z
    return left == right


for x in range(2):
    for y in range(2):
        for z in range(2):
            print(f"x {x} y {y} z {z}")
            print(logical(z, y, z))
