# Семинар 1
import random
# Очистка консоли
import os
def clear(): return os.system('cls')
clear()

# 2. Найти максимальное из пяти чисел
# Получение списка случайных чисел
def get_list_of_random_numbers():
    lst = []
    for i in range(5):
        lst.append(random.randint(0, 100))
    return lst

def find_max_in_five_numbers():
    lst = get_list_of_random_numbers()
    print(f"Список из пяти случайных чисел: {lst}")
    max_number = 0
    for i in lst:
        if i > max_number:
            max_number = i
    print(f"Максимальное число: {max_number}")

find_max_in_five_numbers()