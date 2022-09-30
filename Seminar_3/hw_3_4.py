# Семинар 3
# Очистка консоли
import os


def clear():
    return os.system('cls')


clear()


# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# Преобразование десятичного числа в двоичное
def convert_dec_bin(dec_number):
    temp = dec_number
    bin_number = ''
    while temp > 0:
        bin_number = str(temp % 2) + bin_number
        temp //= 2
    return print(f'Десятичное {dec_number} равно {bin_number} в двоичной системе')

dec_number = int(input('Введите десятичное число '))
convert_dec_bin(dec_number)
print('Второй вариант (через встроенную функцию bin()', end=": ")       #Печать без переноса (символ любой).
                                                                        # По умолчанию перенос на следующую строку.
print(dec_number, bin(dec_number)[2:], sep=' -> ')      #Печать с разделителем (по умолчанию пробел)
# print(type(bin(dec_number)))

