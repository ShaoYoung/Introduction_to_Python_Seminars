# Работа с пользователем в Tkinter

import tkinter as tk
import controller as cont


# import time


def convert_list_to_str(info):
    """
    преобразование списка в строку (для вывода в поле output_info)
    :param phone_book: [(),()]
    :return: str
    """
    info_txt = ''
    if len(info) == 0:
        return info_txt
    else:
        for record in info:
            # record_txt = ' '.join(record)
            record_txt = ' '.join(map(str, record))
            record_txt += '\n'
            info_txt += record_txt
        return info_txt


def start():
    # def print_db():
    #     # lbl_time_info.grid_remove()       #   скрыть виджет
    #     # lbl_time_info.configure(text = 'qwerty')  #  изменить текст (а также любое свойство) виджета
    #     lbl_time_info["text"] = 'qwerty'  # изменить текст (а также любое свойство) виджета   аналогичная запись
    #     listbox1.insert(0, 'строка')

    def print_info(info):
        output_info.delete("1.0", tk.END)
        if len(info) == 0:
            info = 'Ничего не найдено!'
        output_info.insert(tk.END, info)

    def close():
        window.destroy()  # закрытие окна tkinter

    # показать БД
    def show_db():
        info = cont.preview_base_tk()
        info = convert_list_to_str(info)
        print_info(info)

    # чтение данных из entry. на выходе список len(6)
    def read_data():
        correct = lambda x: int(x) if x.isdigit() and int(x) >= 0 else None
        new_record = []
        new_record.append(ent_surname.get())
        new_record.append(ent_name.get())
        new_record.append(ent_gender.get())
        new_record.append(ent_position.get())
        new_record.append(correct(ent_salary.get()))
        new_record.append(correct(ent_bonus.get()))
        return new_record

    # добавить запись в БД
    def add_record():
        # frame_right_down.grid(row=1, column=1, sticky="w")
        # lbl_info.configure(text='Введите данные нового сотрудника')
        new_record = read_data()
        cont.add_db_tk(new_record)

    # frame_right_down.grid_remove()

    # очистка полей ввода
    def clear_entry():
        # output_book.delete("1.0", tk.END)
        ent_surname.delete(0, tk.END)
        ent_name.delete(0, tk.END)
        ent_gender.delete(0, tk.END)
        ent_position.delete(0, tk.END)
        ent_salary.delete(0, tk.END)
        ent_bonus.delete(0, tk.END)

    # поиск информации
    def find_record():
        worker_list = read_data()
        worker_dict = {
            'surname': worker_list[0],
            'name': worker_list[1],
            'gender': worker_list[2],
            'position': worker_list[3],
            'salary': worker_list[4],
            'bonus': worker_list[5],
        }
        info = cont.find_info_tk(worker_dict)
        if len(info) > 0:
            info = convert_list_to_str(info[0])
        print_info(info)

    # удаление информации
    def del_record():
        worker_list = read_data()
        worker_dict = {
            'surname': worker_list[0],
            'name': worker_list[1],
            'gender': worker_list[2],
            'position': worker_list[3],
            'salary': worker_list[4],
            'bonus': worker_list[5],
        }
        cont.del_info_tk(worker_dict)

    window = tk.Tk()
    window.title('Информационная система')
    # Размеры окна
    # window.rowconfigure(0, weight=1)
    # window.rowconfigure(1, weight=1)
    # window.columnconfigure(0, weight=1)
    # window.columnconfigure(1, weight=1)

    # описание виджетов
    # z = time.strftime('%H:%M:%S')
    # рамки
    frame_left_up = tk.Frame(window)
    # lbl_time_info = tk.Label(text='Текущее время')
    btn_show = tk.Button(master=frame_left_up, text='Показать БД', command=show_db)
    btn_add = tk.Button(master=frame_left_up, text='Добавить запись', command=add_record)
    btn_find = tk.Button(master=frame_left_up, text='Найти запись', command=find_record)
    btn_del = tk.Button(master=frame_left_up, text='Удалить запись', bg='red', command=del_record)
    # btn_modify = tk.Button(master=frame_left_up, text='Изменить запись', bg='yellow')
    # btn_stat = tk.Button(master=frame_left_up, text='Статистика')
    # btn_json = tk.Button(master=frame_left_up, text='Сохранить в json', command=save_json)

    frame_left_down = tk.Frame(window)
    btn_close = tk.Button(master=frame_left_down, text='Выход', command=close)

    frame_right_up = tk.Frame(window)
    output_info = tk.Text(master=frame_right_up, width=40)

    frame_right_down = tk.Frame(window)
    lbl_info = tk.Label(master=frame_right_down, text='')
    ent_surname = tk.Entry(master=frame_right_down)
    ent_surname.insert(0, 'Фамилия')
    ent_name = tk.Entry(master=frame_right_down)
    ent_name.insert(0, 'Имя')
    ent_gender = tk.Entry(master=frame_right_down)
    ent_gender.insert(0, 'Пол')
    ent_position = tk.Entry(master=frame_right_down)
    ent_position.insert(0, 'Должность')
    ent_salary = tk.Entry(master=frame_right_down)
    ent_salary.insert(0, 'Зарплата')
    ent_bonus = tk.Entry(master=frame_right_down)
    ent_bonus.insert(0, 'Премия')
    btn_enter = tk.Button(master=frame_right_down, text='Очистить', command=clear_entry)

    # qw = [1,2,3]
    # listbox1 = tk.Listbox(selectmode = 'single')
    listbox1 = tk.Listbox(selectmode='multiple')
    check1 = tk.Checkbutton(text='first')
    # Radiobutton
    # Scale
    # Scrollbar

    # размещение виджетов
    frame_left_up.grid(row=0, column=0, sticky="n")
    btn_show.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    btn_add.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    btn_find.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    btn_del.grid(row=3, column=0, padx=5, pady=5, sticky="w")
    # btn_modify.grid(row=4, column=0, padx=5, pady=5, sticky="w")
    # btn_stat.grid(row=5, column=0, padx=5, pady=5, sticky="w")
    # btn_json.grid(row=6, column=0, padx=5, pady=5, sticky="w")

    frame_left_down.grid(row=1, column=0, sticky="s")
    btn_close.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    frame_right_up.grid(row=0, column=1, sticky="ne")
    output_info.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

    frame_right_down.grid(row=1, column=1, sticky="w")
    lbl_info.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    ent_surname.grid(row=1, column=0, padx=5, pady=5)
    ent_name.grid(row=2, column=0, padx=5, pady=5)
    ent_gender.grid(row=3, column=0, padx=5, pady=5)
    ent_position.grid(row=4, column=0, padx=5, pady=5)
    ent_salary.grid(row=5, column=0, padx=5, pady=5)
    ent_bonus.grid(row=6, column=0, padx=5, pady=5)
    btn_enter.grid(row=7, column=0, padx=5, pady=5, sticky="e")
    # lbl_time_info.grid(row=0, column=0, padx=5, pady=5)
    # listbox1.grid(row=1, column=0, padx=5, pady=5)
    # check1.grid(row=1, column=1, padx=5, pady=5)

    window.mainloop()
