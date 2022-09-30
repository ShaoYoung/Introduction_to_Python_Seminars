# Семинар 3
# Очистка консоли
import os


def clear():
    return os.system('cls')


clear()


# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]
# в условии задачи ошибка. Первое число Фибоначчи = 0, второе 1, третье 1 ... восьмое 13, девятое 21 и т.д.
# F(−n) = (−1)^(n+1) * Fn
# Fn = F(n+2)−F(n+1)

# Нахождение n-го числа Фибоначчи
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


# Негафибоначчи
def nega_fibonacci(n):
    list_negafibonacci = []
    for i in range(1, n + 1):
        fibo_i = fibonacci(i)
        list_negafibonacci.append(fibo_i)  # добавляем в конец списка очередное число Фибоначчи
        if i != 1:  # если не первое число Фибоначчи, то
            list_negafibonacci.insert(0, (-1) ** (i) * fibo_i)#добавляем в начало списка очередное число Негафибоначчи
    print(f'Негафибоначчи: {list_negafibonacci}')


n = int(input('Введите количество чисел Фибоначчи: '))
nega_fibonacci(n)
