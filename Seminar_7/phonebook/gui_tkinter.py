# GUI Tkinter

import tkinter_work as tk

window = tk.Tk()
window.title('Телефонный справочник')


# frame_a = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)

# frame_a.grid(row = 0, column = 0, padx=10, pady=10)
# label = tk.Label(master=frame_a, text="Привет, Tkinter!")
# label.pack(padx=10, pady=10)

# def click(event):
#     print('Нажата кнопка!')

def click_1(text):
    print(text)


def click_2(text):
    print(text)


# def handle_click(event):
#     print("Нажата кнопка!")
#
#
# button = tk.Button(text="Кликни!")
#
# button.bind("<Button-1>", handle_click)   # ЛКМ


# frame_b = tk.Frame(master=window, relief=tk.RAISED, borderwidth=1)
# frame_b.grid(row = 0, column = 1, padx=10, pady=10)
# button = tk.Button(master=frame_b, text="Привет, Tkinter!", command=click_2())
# Для вызова обработчика событий во время возникновения события, связанного с виджетом, используется метод .bind().
# button.bind('<Button-1>', click)
button_1 = tk.Button(master=window, text="file_type", command=click_1('file_type'))
button_1.grid(row=0, column=1)

button_2 = tk.Button(master=window, text="action", command=click_2('action'))
button_2.grid(row=1, column=1)

# Виджеты Label используется для отображения текста или картинок.
# label = tk.Label(master=frame_a, text="Привет, Tkinter!")
# label = tk.Label(
#     text="Привет, Tkinter!",
#     fg="white",
#     bg="black",
#     width=20,
#     height=20
# )
# label.pack()
# label.place()
# При использовании метода .pack() для размещения виджета в окне,
# Tkinter устанавливает размер окна настолько маленьким, насколько возможно, пока в него не влезает виджет.


# Button нужны для создания кликабельных кнопок.
# Их можно настроить таким образом, чтобы при нажатии вызывалась определенная функция
# button = tk.Button(master=frame_b, text='Кнопка')
#     text="Нажми на меня!",
#     width=50,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )
# button.pack()

# В случаях, когда требуется получить текстовую информацию (однострочную) от пользователя,
# используется виджет Entry. Он отображает небольшой текстовый бокс, куда пользователь может ввести текст.
# Получение всего текста через .get()
# Удаление текста через .delete()
# Вставка нового текста через .insert()

# entry = tk.Entry(fg="yellow", bg="blue", width=50)
# entry = tk.Entry(master=frame_b)
# entry.pack()

# entry.insert(0, "Иванов")


# Виджет Text — ввод большого текста в Tkinter
# Как и в случае с виджетами Entry, над виджетами Text можно провести три основные операции:
# Получение текста через метод .get()
# Удаление текста через метод .delete()
# Вставка текста через метод .insert()
# Для получения нескольких символов требуется передать начальный и конечный индексы.
# Номера строк начинаются с 1, а позиция символа с 0
# К примеру, "1.0" означает первый символ на первой строке, а "2.3" представляет четвертый символ на второй строке.
# Для получения всего текста из текстового виджета установите индекс на "1.0"
# и используйте специальную константу tk.END для второго индекса text_box.get("1.0", tk.END)

# text_box = tk.Text()
# text_box.pack()


# window.mainloop() указывает Python, что нужно запустить цикл событий Tkinter
# он также блокирует запуск любого кода, что следует после, пока окно, на котором оно было вызвано, не будет закрыто
window.mainloop()

# закрытие предыдущего окна
# window.destroy()


# name = entry.get()
# print(name)
