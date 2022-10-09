# Семинар 4
# Очистка консоли
import os


def clear():
    return os.system('cls')


clear()


# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


# Проверка на простое число. Возвращает True если число простое, и False если нет
def check_simple(n):
    for i in range(2, (n // 2 + 1)):
        # Если делится без остатка на любое число из диапазона n/2, то число не простое
        if (n % i == 0):
            return False
    return True


# Разложение натурального числа на простые множители. Возвращает список простых множителей.
def simple_multipliers(n):
    if n < 2:
        return
    simple_numbers = []
    # поочередно целочисленно делим число на 2...n
    # while n > 1:
    for i in range(2, n + 1):
        # если делится нацело, то проверяем делитель на простое число
        if n % i == 0:
            # если делитель - простое число, добавляем его в список
            if check_simple(i):
                simple_numbers.append(i)
                # n //= i
                # break
    return simple_numbers

# Разложение числа на простые множители
def split_simple_multipliers(n):
    if n < 2:
        return
    simple_numbers = []
    # поочередно целочисленно делим число на 2...n
    while n > 1:
        for i in range(2, n + 1):
            # если делится нацело, то проверяем делитель на простое число
            if n % i == 0:
                # если делитель - простое число, добавляем его в список
                if check_simple(i):
                    simple_numbers.append(i)
                    n //= i
                    break
    return simple_numbers




n = abs(int(input("Введите натуральное число: ")))
print(f"Список простых множителей числа {n}: {simple_multipliers(n)}")
print(f"Разложение на простые множители числа {n}: {split_simple_multipliers(n)}")

# n = int(input("Введите натуральное число: "))
# проверка на принадлежность экземпляра object классу classinfo. Возвращает bool
# if isinstance(object, classinfo):
#     n = abs(int(n))
#     print(f"Список простых множителей числа {n}: {simple_multipliers(n)}")
# else:
#     print("Некорректный ввод!")

# количество знаков (разрядность) в десятичном числе
# print(len(str(n)))
