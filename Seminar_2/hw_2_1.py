# Семинар 2
# Очистка консоли
import os


def clear():
    return os.system('cls')


clear()


# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
# 1. Подсчитать сумму цифр в вещественном числе.

# Первый вариант (через удаление точки, м.б. запятой и знака)
def sum_of_numbers(n):
    sum_numb = 0;
    if n.find(',') > -1:
        n = n.replace(',', '', 1)
    if n.find('.') > -1:
        n = n.replace('.', '', 1)
    if n.find('-') > -1:
        n = n.replace('-', '', 1)
    if not n.isdigit():
        print("Некорректный ввод!")
    else:
        for i in n:
            sum_numb += int(i)
    return sum_numb


# Второй вариант (через поэлементный перебор строки и проверку элемента на цифру)
# без проверки на корректный ввод, просто суммирует цифры
def sum_of_numbers_var_2(n):
    sum_numb = 0;
    for i in n:
        if i.isdigit():
            sum_numb += int(i)
    return sum_numb


n = input("Введите вещественное число ")
print(f"Сумма цифр числа {n} равна {sum_of_numbers(n)}")
print(f"Сумма цифр числа {n} равна {sum_of_numbers_var_2(n)}")

sum_numbers = sum(map(int, (filter(lambda x: x.isdigit(), n))))
# sum_numbers = sum(map(int, sum_numbers))
print(f'Сумма цифр числа {n} равна {sum_numbers} (третий вариант через filter и map)')
