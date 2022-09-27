# Семинар 2
# Очистка консоли
import os
import random


def clear():
    return os.system('cls')


clear()


# 5. Реализовать алгоритм перемешивания списка
# Реализовано: чёт <-> нечет, произвольный микс, сортировка прямо и обратно, список соответствия символа его коду

# Создание random-списка натуральных чисел (соответствуют коду заглавных букв латинского алфавита)
def get_list_numbers(n):
    list_numbers = []
    for i in range(n):
        list_numbers.append(random.randint(ord('A'), ord('Z')))
    return (list_numbers)


# Создание списка соответствия символа его коду
def get_list_mapping(list_numbers):
    list_code_symbol = []
    for code in list_numbers:
        list_code_symbol.append(code)
        list_code_symbol.append(chr(code))
    return list_code_symbol


# Меняет местами элементы, стоящие на чётных и нечётных позициях
def honest(list_numbers):
    for i in range(0, len(list_numbers), 2):
        list_numbers[i], list_numbers[i + 1] = list_numbers[i + 1], list_numbers[i]
    return list_numbers


# Произвольно перемешивает список
def mix_list(list_numbers):
    for i in range(0, len(list_numbers)):
        # удаляем последний элемент списка и записываем его в number
        number = list_numbers.pop()
        # вставляем элемент из number на произвольную позицию списка
        list_numbers.insert(random.randint(0, len(list_numbers)), number)
    return list_numbers

# длина списка
n = 10
list_numbers = get_list_numbers(n)
print(f"Исходный список натуральных чисел: {list_numbers}")
print(f"Список, с заменой чёт/нечет-позиций: {honest(list_numbers)}")
print(f"Произвольно перемешанный список: {mix_list(list_numbers)}")
list_numbers.sort(reverse=True)
print(f"Список, сортированный в обратном порядке (по убыванию): {list_numbers}")
list_numbers.reverse()
print(f"Развёрнутый список (теперь по возрастанию): {list_numbers}")
print(f"Список соответствия символа его коду (код, символ): {get_list_mapping(list_numbers)}")
