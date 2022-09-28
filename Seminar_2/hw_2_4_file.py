# Семинар 2
# Очистка консоли
import os


def clear():
    return os.system('cls')


clear()


# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# Создание списка от -n до n
def get_list(n):
    list_interval = []
    for i in range(-n, n + 1):
        list_interval.append(i)
    return (list_interval)


# Запись позиций списка в файл
def write_file(file_name, len_list):
    correct_input = False
    position_list = []
    # ввод позиций списка для последующей их записи в файл (с проверкой)
    while not correct_input:
        correct_input = True
        position = input(f"Записываем файл позиций. Введите позиции элементов списка (целые числа через запятую) ")
        position_list = position.split(',')
        for i in position_list:
            if (not i.isdigit()) or (int(i) > (len_list - 1) or int(i) < 0):
                correct_input = False
                print("Некорректный ввод")
                break
    # print(position_list)
    # записываем файл с позициями списка. каждая позиция на отдельной строке
    f = open(file_name, 'w')
    for i in position_list:
        f.write(i + '\n')
    f.close()
    # return


# Чтение позиций списка из файла
def read_file(file_name):
    position_list = []
    # f = open(file_name, 'r')
    # альтернативный вариант. в этом случае файл закрывается автоматически
    with open(file_name, 'r') as f:
        for line in f:
            position_list.append(int(line))
    return position_list


# Умножение элементов. На входе два списка. Первый с элементами, второй с номерами позиций
def multi_position(list_interval, position_list):
    multi = 1
    for i in position_list:
        multi *= list_interval[i]
    return multi


file_name = 'file.txt'
n = int(input("Введите число N "))
list_interval = get_list(n)
print(f"Список от {-n} до {n} {list_interval}")
write_file(file_name, len(list_interval))
position_list = read_file(file_name)
print(f"Произведение элементов списка на указанных позициях равно {multi_position(list_interval, position_list)}")
