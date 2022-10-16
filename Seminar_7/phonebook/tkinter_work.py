import tkinter as tk
import file as f
import change_db as chdb


def convert_list_to_str(phone_book):
    """
    преобразование списка в строку (для вывода в поле output_book)
    :param phone_book: [[],[]]
    :return: str
    """
    book_txt = ''
    if len(phone_book) == 0:
        return book_txt
    else:
        for abonent in phone_book:
            ab_record = ' '.join(abonent)
            ab_record += '\n'
            book_txt += ab_record
        return book_txt


def start():
    def print_info(info):
        output_book.delete("1.0", tk.END)
        if len(info) == 0:
            info = 'Ничего не найдено!'
        output_book.insert(tk.END, info)

    def read_pickle():
        phone_book = f.read_pickle()
        phone_book = convert_list_to_str(phone_book)
        print_info(phone_book)

    def find_info():
        detected_abonent = ''
        find_info = ent_find_info.get()
        if len(find_info) > 0:
            detected_abonent = chdb.find_in_file(find_info)
            detected_abonent = convert_list_to_str(detected_abonent)
        print_info(detected_abonent)

    def add_info():
        new_abonent = []
        new_abonent.append(ent_add_surname.get())
        new_abonent.append(ent_add_name.get())
        new_abonent.append(ent_add_tel.get())
        new_abonent.append(ent_add_comm.get())
        phone_book = f.read_file()
        phone_book.append(new_abonent)
        f.save_file(phone_book)
        print_info('Добавлено!')

    def show_del_info():
        detected_abonent = ''
        find_info = ent_del_info.get()
        if len(find_info) > 0:
            detected_abonent = chdb.find_in_file(find_info)
            detected_abonent = convert_list_to_str(detected_abonent)
        print_info(detected_abonent)

    def del_info():
        del_info = ent_del_info.get()
        if not chdb.remove_element(del_info):
            print_info('Не могу удалить!')
        else:
            print_info('Удалено!')

    def save_txt():
        phone_book = f.read_pickle()
        f.save_file(phone_book, file_type=1)
        print_info('Справочник сохранён!')

    def save_csv():
        phone_book = f.read_pickle()
        f.save_file(phone_book, file_type=2)
        print_info('Справочник сохранён!')

    def save_json():
        phone_book = f.read_pickle()
        f.save_file(phone_book, file_type=3)
        print_info('Справочник сохранён!')

    def save_html():
        phone_book = f.read_pickle()
        f.save_file(phone_book, file_type=5)
        print_info('Справочник сохранён!')

    window = tk.Tk()
    window.title("Телефонный справочник")

    # Размеры окна
    window.rowconfigure(0, minsize=550, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    # Описание виджетов
    output_book = tk.Text(window)
    frame_left = tk.Frame(window)
    btn_open_pickle = tk.Button(master=frame_left, text='Показать справочник', command=read_pickle)
    lbl_find_info = tk.Label(master=frame_left, text='Поиск информации')
    ent_find_info = tk.Entry(master=frame_left)
    btn_find_info = tk.Button(master=frame_left, text='Найти абонента', command=find_info)
    lbl_add_info = tk.Label(master=frame_left, text='Добавление информации')
    ent_add_surname = tk.Entry(master=frame_left)
    ent_add_surname.insert(0, 'Фамилия')
    ent_add_name = tk.Entry(master=frame_left)
    ent_add_name.insert(0, 'Имя')
    ent_add_tel = tk.Entry(master=frame_left)
    ent_add_tel.insert(0, 'Телефон')
    ent_add_comm = tk.Entry(master=frame_left)
    ent_add_comm.insert(0, 'Комментарий')
    btn_add_info = tk.Button(master=frame_left, text='Добавить абонента', bg='green', fg='white', command=add_info)
    lbl_del_info = tk.Label(master=frame_left, text='Удаление информации')
    ent_del_info = tk.Entry(master=frame_left)
    btn_show_info = tk.Button(master=frame_left, text='Показать', bg='yellow', command=show_del_info)
    btn_del_info = tk.Button(master=frame_left, text='Удалить', bg='red', command=del_info)
    lbl_save_info = tk.Label(master=frame_left, text='Сохранение информации', fg='blue')
    btn_save_txt = tk.Button(master=frame_left, text='Сохранить в txt', command=save_txt)
    btn_save_csv = tk.Button(master=frame_left, text='Сохранить в csv', command=save_csv)
    btn_save_json = tk.Button(master=frame_left, text='Сохранить в json', command=save_json)
    btn_save_html = tk.Button(master=frame_left, text='Сохранить в html', command=save_html)

    # Размещение виджетов
    btn_open_pickle.grid(row=0, column=0, padx=5, pady=5)
    lbl_find_info.grid(row=1, column=0, padx=5, pady=5)
    ent_find_info.grid(row=2, column=0, padx=5, pady=5)
    btn_find_info.grid(row=2, column=1, padx=5, pady=5)
    lbl_add_info.grid(row=4, column=0, padx=5, pady=5)
    ent_add_surname.grid(row=5, column=0, padx=5, pady=5)
    ent_add_name.grid(row=6, column=0, padx=5, pady=5)
    ent_add_tel.grid(row=7, column=0, padx=5, pady=5)
    ent_add_comm.grid(row=8, column=0, padx=5, pady=5)
    btn_add_info.grid(row=8, column=1, padx=5, pady=5)
    lbl_del_info.grid(row=10, column=0, padx=5, pady=5)
    ent_del_info.grid(row=11, column=0, padx=5, pady=5)
    btn_show_info.grid(row=11, column=1, padx=5, pady=5)
    btn_del_info.grid(row=12, column=1, padx=5, pady=5)
    lbl_save_info.grid(row=13, column=0, padx=5, pady=5)
    btn_save_txt.grid(row=14, column=0, padx=5, pady=5)
    btn_save_csv.grid(row=15, column=0, padx=5, pady=5)
    btn_save_json.grid(row=16, column=0, padx=5, pady=5)
    btn_save_html.grid(row=17, column=0, padx=5, pady=5)

    frame_left.grid(row=0, column=0, sticky="ns")
    output_book.grid(row=0, column=1, sticky="nsew")

    window.mainloop()
