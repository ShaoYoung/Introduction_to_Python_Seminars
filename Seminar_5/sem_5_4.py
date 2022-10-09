# Семинар 5
# 4. Создайте программу для игры с конфетами человек против человека.
#     Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#     Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
#     Все конфеты оппонента достаются сделавшему последний ход.
#     Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#     a) Добавьте игру против бота
#     b) Подумайте как наделить бота "интеллектом"

# для тестирования брать малое число
# два игрока. Имена.
# Первый ход рандомно.
# Обращение к игроку. Возьмите со стола от 1 до 28 конфет. Проверка от 1 до 28, иначе повтор.
# Потом ко второму игроку.
# Отображать оставшееся число конфет.
#
# Бот. Второй игрок. Забирает рандомно.
#
# Умный бот. Надо на предпоследнем шаге оставить 29 конфет. Определять уровень интеллекта бота.

import random


# слово "конфета" с правильными окончаниями
def ending(n, variant=1):
    if n % 100 in [0, 10, 11, 12, 13, 14]:
        return 'конфет'
    elif n % 10 in [2, 3, 4]:
        return 'конфеты'
    elif n % 10 in [1] and variant:
        return 'конфета'
    elif n % 10 in [1] and not variant:
        return 'конфету'
    elif n % 10 in [0, 5, 6, 7, 8, 9]:
        return 'конфет'


# Цвет текста и фона, стиль текста в консоли
# \033[1m - жирный
# \033[3m - курсив
# \033[4m - подчёркнутый
# \033[0m - возврат к начальным значениям
# \033[30m - \033[37m - цвет текста
# \033[40m - \033[47m - цвет текста фона

start_candy = 2021
print('Давайте сыграем в конфеты!!! Правила игры следующие:')
print(
    f'На столе лежит {start_candy} {ending(start_candy)}. Играют два игрока (или игрок с ботом), делая ход друг после друга.')
print('Первый ход определяется жеребьёвкой. За один ход можно забрать не более, чем 28 конфет.')
print('Все конфеты противника достаются игроку, сделавшему последний ход.')
input_true = False
while not input_true:
    bot = input('Выберите вариант игры (0 - играют два игрока, 1 - человек играет с ботом.): ')
    if not bot.isdigit() or int(bot) not in (0, 1):
        input_true = False
        print('Вы ошиблись при вводе! Попробуйте ещё раз.')
    else:
        bot = int(bot)
        input_true = True
players = {False: '', True: ''}
if bot:
    players[False] = input('Введите ваше имя: ')
    bot_level = int(input('Введите уровень интеллекта бота (цифру от 1 до 3): '))
    if bot_level == 3 or bot_level not in (1, 2, 3):
        print('\033[1m\033[33mС вами будет играть самый крутой бот!!!\033[0m')
        bot_level = 3
    players[True] = 'Bot'
else:
    players[False] = input('Введите имя первого игрока: ')
    players[True] = input('Введите имя второго игрока: ')

# players[False] = 'Человек'
# players[True] = 'Bot'
# bot = 1
# bot_level = 2


print(f'Итак, играют {players[False]} и {players[True]}')

# start_candy = 150
candy = start_candy

# рандомно определяем право первого хода
attempt = bool(random.getrandbits(1))
while candy > 0:
    print(f'На столе {candy} {ending(candy)}. Очередь игрока \033[1m\033[31m{players[attempt]}\033[0m.')
    # если играет bot и его очередь ходить
    if bot and attempt:
        # у бота средний уровень интеллекта. расчёт включается (повышается уровень интеллекта) только после экватора.
        if bot_level == 2 and start_candy / candy > 2:
            bot_level = 3
        # бот очень "умный", сразу считает нужное количество конфет
        if bot_level == 3:
            if 1 < candy < 29:
                get_candy = candy
            else:
                # bot берёт "нужное" для победы количество конфет
                get_candy = candy % 29
                # если не вышло, то на текущем шаге количество конфет выбирается случайно
                if not get_candy:
                    get_candy = random.randint(1, min(candy, 28))
        # у бота нет интеллекта, количество конфет всегда определяется случайно
        else:
            get_candy = random.randint(1, min(candy, 28))
        print(f'{players[attempt]} взял {get_candy} {ending(get_candy, 0)}')
        candy -= int(get_candy)
        attempt = not attempt
    else:
        input_true = False
        while not input_true:
            print(f'Возьмите от 1 до {min(candy, 28)} {ending(min(candy, 28), 0)}.')
            get_candy = input('-OO- ')
            if not get_candy.isdigit() or not 1 <= int(get_candy) <= min(candy, 28):
                print(
                    f'Некорректный ввод! Вы вводите {get_candy}, а надо целое число от 1 до {min(candy, 28)}. Попробуйте ещё раз!')
            else:
                input_true = True
                candy -= int(get_candy)
                attempt = not attempt
print(f'Выиграл \033[1m\033[31m{players[not attempt]}\033[0m. \033[3m\033[31mПоздравляю!\033[0m')
