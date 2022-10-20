import sqlite3
bd = sqlite3.connect('Data_dase.db')
cursor = bd.cursor()
# НАЙТИ АВТОИНКРЕМЕНТ id !!!!!!!
cursor.execute('''CREATE TABLE IF NOT EXISTS personal(
    id INTEGER PRIMARY KEY autoincrement,           
    name TEXT,
    last_name TEXT,
    position TEXT,
    salary INT,
    bonus INT)'''
)
baza = [(1, 'Иван','Иванов','главный инженер',50000, 10000),
        (2, 'Иван','Семенов','инженер',20000, 8000),
        (3, 'Олег','Петров','завхоз',120000, 3000)]
# baza = [('Иван','Иванов','главный инженер',50000, 10000),
#         ('Иван','Семенов','инженер',20000, 8000),
#         ('Олег','Петров','завхоз',120000, 3000)]


try:
    cursor.executemany('INSERT INTO personal VALUES (?,?,?,?,?,?);', baza)
    bd.commit()
except:
    print('Данные уже есть')



# cursor.execute('DELETE from personal WHERE id=1')
# for i in cursor.execute('SELECT * FROM personal'):
#     print(*i)
cursor.execute('SELECT * FROM personal WHERE name="Олег";')
many = cursor.fetchone()
print(many)


cursor.execute('DELETE from personal WHERE id=1')
for i in cursor.execute('SELECT * FROM personal'):
    print(*i)


def preview_base():
    cursor.execute('SELECT * FROM personal')
    many = cursor.fetchall()
    print(many)
    # for i in cursor.execute('SELECT * FROM personal'):
    #     print(*i)

def add_record():
    pass

def find_record(column, name):
    # pass          заглушка
    cursor.execute(f'SELECT * FROM personal WHERE {column} LIKE {name}')
    one = cursor.fetchmany()
    return one

def delete_record(id):
    cursor.execute(f'DELETE from personal WHERE id={1}')
    bd.commit()

# цикл работает до break
def input_choice():
    while True:
        user_choice = input('1 - просмотреть базу, 2 - добавить запись, 3 - удалить запись,'
                            ' 4 - найти сотрудника, q - выход: ')
        if user_choice == '1':
            preview_base()
        elif user_choice == '2':
            preview_base()
        elif user_choice == '3':
            delete_record()
        elif user_choice == '4':
            find_record()
        elif user_choice == 'q':
            print('Выход')
            break
        else:
            print('Не верно введён режим работы')

# input_choice()

# изменение данных в БД
cursor.execute('UPDATE personal SET salary = 55000 WHERE id=2;')
bd.commit()
for i in cursor.execute('SELECT * FROM personal'):
    print(*i)


# cur = conn.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS workers(
#    workerid INT PRIMARY KEY,
#    surname TEXT,
#    name TEXT,
#    gender TEXT,
#    age TEXT);
# """)
# conn.commit()
# workers = [('00001', 'Иванов', 'Иван', 'мужчина', '45')]
# cur.executemany("INSERT INTO workers VALUES(?, ?, ?, ?);", workers)
# 
# cur.execute("select * from orders")
# print(*cur.fetchall(), sep='\n')
# 
# 
