# Семинар 3
# Очистка консоли
import os


def clear():
    return os.system('cls')


clear()


# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# Задание списка строк
def input_string():
    list_string = input(f"Введите список строк (строки через пробел) ")
    list_string = list_string.split(' ')
    return list_string


def find_numbers_in_list(list_string, number):
    for item in list_string:
        if number in item:  # поиск подстроки в строке (элементе списка)
            # return True
            print(f'В элементе списка {item} есть число {number}')
        # elem = item
        # if not (item.find(',') > -1 and elem.find('.') > -1):   #если нет сразу . и ,:
        #     if item.find(',') > -1:                 #если есть ',' убираем
        #         elem = item.replace(',', '', 1)
        #     if elem.find('.') > -1:                 #если есть '.' убираем
        #         elem = elem.replace('.', '', 1)
        # if elem.find('-') > -1:                 #если есть '-' убираем
        #     elem = elem.replace('-', '', 1)
        # if elem.isdigit():                      #если остались только цифры, то есть число
        #     print(f'В списке есть число {item}')
    return


list_string = input_string()
print(f'Список строк {list_string}')
number = input('Введите число, которое вы хотите найти в списке ')
find_numbers_in_list(list_string, number)
