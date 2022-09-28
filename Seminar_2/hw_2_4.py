# Семинар 2
# Очистка консоли
import os


def clear():
    return os.system('cls')


clear()


# 4. Задать список из N элементов, заполненных числами из [-N, N].
# Найти произведение элементов на указанных позициях.
# Позиции хранятся в списке positions - создайте этот список (например: positions = [1, 3, 6]).
# Создание списка от -n до n
def get_list(n):
    list_interval = []
    for i in range(-n, n + 1):
        list_interval.append(i)
    return (list_interval)


# Запись позиций списка в отдельный список. на входе длина имеющегося списка.
def write_list_positions(len_list):
    correct_input = False
    positions = []
    # ввод позиций списка (с проверкой)
    while not correct_input:
        correct_input = True
        positions_string = input(f"Введите позиции элементов списка (целые числа через запятую) ")
        positions = positions_string.split(',')
        # проверка на корректность ввода
        for i in positions:
            if (not i.isdigit()) or (int(i) > (len_list - 1) or int(i) < 0):
                correct_input = False
                print("Некорректный ввод")
                break
    # print(position_list)
    return positions


# Умножение элементов. На входе два списка. Первый с элементами, второй с номерами позиций
def multi_position(list, position_list):
    multi = 1
    for i in position_list:
        multi *= list[int(i)]
    return multi


n = int(input("Введите число N: "))
list_interval = get_list(n)
print(f"Список от {-n} до {n} {list_interval}")
position_list = write_list_positions(len(list_interval))
print(f"Произведение элементов списка на указанных позициях равно {multi_position(list_interval, position_list)}")
