# Начало
import view_terminal as vt
import view_tkinter as tk
import controller as cont

# цикл работает до break
def input_var_work():
    cont.start_work()
    while True:
        user_choice = input('0 - Консольный вариант работы БД \n1 - Tkinter-вариант работы БД \nq - Выход \n-->> ')
        # user_choice = '1'
        if user_choice == '0':
            vt.input_action()
        elif user_choice == '1':
            tk.start()
        elif user_choice == 'q':
            print('Завершение работы')
            break
        else:
            print('Не верно введён режим работы!')

input_var_work()

