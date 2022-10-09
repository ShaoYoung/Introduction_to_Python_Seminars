# Семинар 5
# 5. Создайте программу для игры в "Крестики-нолики".

# поле 3х3
#
# Вложенный список (список списков)
# Красивый вывод. 2 вложенных цикла
# Пользователь вводит координаты от 0,0 до 3,3
# Проверять занятые клетки
# После каждого хода отображать игровое поле
# Проверять заполнение горизонтали/вертикали/основной диагонали/второстепенной диагонали

import random


# Отображение игрового поля. На входе список списков.
def print_playing_field(matrix):
    print('\033[32mСейчас игровое поле выглядит так:\033[0m')
    print(f'\033[4m  0 1 2 \033[0m\n', end='')
    row_number = 0
    for row in matrix:
        print(row_number, end='')
        row_number += 1
        for column in row:
            print(f'\033[4m|{column}\033[0m', end='')
        print('\033[4m|\033[0m')


# Проверка на строку, столбец, главную диагональ, второстепенную диагональ
def check_winner(matrix):
    var_win = []
    # варианты победы
    var_win.append(matrix[0][0] == matrix[0][1] == matrix[0][2] != ' ')
    var_win.append(matrix[1][0] == matrix[1][1] == matrix[1][2] != ' ')
    var_win.append(matrix[2][0] == matrix[2][1] == matrix[2][2] != ' ')
    var_win.append(matrix[0][0] == matrix[1][0] == matrix[2][0] != ' ')
    var_win.append(matrix[0][1] == matrix[1][1] == matrix[2][1] != ' ')
    var_win.append(matrix[0][2] == matrix[1][2] == matrix[2][2] != ' ')
    var_win.append(matrix[0][0] == matrix[1][1] == matrix[2][2] != ' ')
    var_win.append(matrix[0][2] == matrix[1][1] == matrix[2][0] != ' ')
    # print(var_win)
    if var_win.count(True) > 0:
        return True
    return False


print('Давайте сыграем в крестики-нолики!!!')
players = {False: '', True: ''}
players[False] = input('Введите имя первого игрока: ')
players[True] = input('Введите имя второго игрока: ')
# players[False] = 'Игрок_1'
# players[True] = 'Игрок_2'

print(f'Итак, играют {players[False]} - \033[1m\033[31m0\033[0m и {players[True]} - \033[1m\033[31mX\033[0m')
# рандомно определяем право первого хода
attempt = bool(random.getrandbits(1))
attempt_number = 0
# стартовое игровое поле
matrix = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

while not check_winner(matrix) and attempt_number < 9:
    print_playing_field(matrix)
    print(f'Очередь игрока \033[1m\033[31m{players[attempt]}\033[0m.')
    if attempt:
        marker = 'X'
    else:
        marker = '0'
    input_true = False
    while not input_true:
        print(f'Введите координаты вашего {marker} (две цифры от 0 до 2, разделённые пробелом)')
        coord = input(f'{marker} -- ')
        # если игрок ошибочно не ввёл разделитель (пробел)
        if coord.find(' ') == -1 or len(coord) < 3:
            print('Некорректный ввод! Попробуйте ещё раз!')
        else:
            # разбиваем и проверяем
            coord = coord.split()
            if not coord[0].isdigit() or not coord[1].isdigit() or not 0 <= int(coord[0]) <= 2 or not 0 <= int(
                    coord[1]) <= 2:
                print('Некорректный ввод! Попробуйте ещё раз!')
            else:
                coord = list(map(int, coord))
                if matrix[coord[0]][coord[1]] in ('X', '0'):
                    print(f'Эта ячейка игрового поля уже занята. На ней стоит {matrix[coord[0]][coord[1]]}.')
                else:
                    matrix[coord[0]][coord[1]] = marker
                    attempt_number += 1
                    input_true = True
                    attempt = not attempt
if attempt_number < 9:
    print(f'Выиграл \033[1m\033[31m{players[not attempt]}\033[0m. \033[3m\033[31mПоздравляю!\033[0m')
else:
    print('\033[1m\033[31mБоевая ничья!\033[0m')

print_playing_field(matrix)
