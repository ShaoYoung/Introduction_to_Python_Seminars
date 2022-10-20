import sqlite3
# Opens a connection to the SQLite database file *database*
# Функция connect создает соединение с базой данных SQLite и возвращает объект, представляющий ее.
conn = sqlite3.connect('orders.db')
# Еще один способ создания баз данных с помощью SQLite в Python — создание их в памяти.
# БД существует только в оперативной памяти.
# conn = sqlite3.connect(:memory:)
# После создания объекта соединения с базой данных нужно создать объект cursor.
# Он позволяет делать SQL-запросы к базе. Используем переменную cur для хранения объекта:
cur = conn.cursor()
# Теперь выполнять запросы можно следующим образом:
# cur.execute("ВАШ-SQL-ЗАПРОС-ЗДЕСЬ;")
# Запросы должны быть помещены в кавычки. Это могут быть одинарные, двойные или тройные кавычки.
# Последние используются в случае особенно длинных запросов, которые часто пишутся на нескольких строках.

# создание таблицы users
# Функция execute отвечает за SQL-запрос, SQL генерирует таблицу users
# IF NOT EXISTS поможет при попытке повторного подключения к базе данных. Запрос проверит, существует ли таблица.
# Если да — проверит, ничего ли не поменялось.
# Создаем первые четыре колонки: userid, fname, lname и gender. Userid — это основной ключ.
# Сохраняем изменения с помощью функции commit для объекта соединения.
cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
conn.commit()

# создание таблицы orders
cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   orderid INT PRIMARY KEY,
   date TEXT,
   userid TEXT,
   total TEXT);
""")
conn.commit()
# ===================================
# Добавление данных с SQLite в Python
# ===================================
# cur.execute("""INSERT INTO users(userid, fname, lname, gender)
#    VALUES('00001', 'Alex', 'Smith', 'male');""")
# conn.commit()
# или ЧЕРЕЗ ПЕРЕМЕННЫЕ, в которых хранятся значения. Например, это может быть кортеж с информацией о пользователе
# user = ('00002', 'Lois', 'Lane', 'Female')
# cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
# conn.commit()
# В данном случае все значения заменены на знаки вопроса и добавлен параметр, содержащий значения, которые нужно добавить.
# SQLite ожидает получить значения в формате кортежа. Однако в переменной может быть и список с набором кортежей.
# Таким образом можно добавить несколько пользователей:
# more_users = [('00003', 'Peter', 'Parker', 'Male'), ('00004', 'Bruce', 'Wayne', 'male')]
# Но нужно использовать функцию executemany вместо обычной execute:
# cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)
# conn.commit()
# Использование способа с вопросительными знаками (?, ?, …) также помогает противостоять SQL-инъекциям.
# Поэтому рекомендуется использовать его, а не упомянутый до этого.
# Переменные для добавления данных в обе таблицы:
customers = [
  ('00005', 'Stephanie', 'Stewart', 'female'), ('00006', 'Sincere', 'Sherman', 'female'), ('00007', 'Sidney', 'Horn', 'male'),
  ('00008', 'Litzy', 'Yates', 'female'), ('00009', 'Jaxon', 'Mills', 'male'), ('00010', 'Paul', 'Richard', 'male'),
  ]
orders = [
  ('00001', '2020-01-01', '00025', '178'), ('00002', '2020-01-03', '00025', '39'), ('00003', '2020-01-07', '00016', '153'),
  ('00004', '2020-01-10', '00015', '110'), ('00005', '2020-01-11', '00024', '219'), ('00006', '2020-01-12', '00029', '37'),
  ('00007', '2020-01-14', '00028', '227'), ('00008', '2020-01-18', '00010', '232'), ('00009', '2020-01-22', '00016', '236'),
  ('00010', '2020-01-26', '00017', '116'), ('00011', '2020-01-28', '00028', '221'), ('00012', '2020-01-31', '00021', '238'),
]
# сохранить обе переменные в обе таблицы
# cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", customers)
# cur.executemany("INSERT INTO orders VALUES(?, ?, ?, ?);", orders)
# conn.commit()
# ===================================
# Получение данных с SQLite в Python
# ===================================
# fetchone() - получение только одного результата
# cur.execute("SELECT * FROM users;")
# one_result = cur.fetchone()
# print(one_result)

# fetchmany() - получение нескольких результатов, например fetchmany(3). На выходе список кортежей.
# cur.execute("SELECT * FROM users;")
# three_results = cur.fetchmany(3)
# print(three_results)

# fetchall() - получение всех результатов
# cur.execute("SELECT * FROM users;")
# all_results = cur.fetchall()
# print(*all_results, sep='\n')
# cur.execute("SELECT * FROM orders;")
# all_results = cur.fetchall()
# print(*all_results, sep='\n')
# cur.execute("SELECT * FROM users;")
# all_results = cur.fetchall()
# print(*all_results, sep='\n')

# cur.execute("select * from users where gender = 'Male';")
# all_result = cur.fetchall()
# print(all_result, sep='\n')

# cur.execute("delete from users where gender = 'Male';")
# conn.commit()
# cur.execute("select * from users where gender = 'Male'")
# print(cur.fetchall(), sep='\n')

# Объединение таблиц в SQLite в Python
# cur.execute("""SELECT *, users.fname, users.lname FROM orders JOIN users ON users.userid=orders.userid;""")
# print(cur.fetchall())

# cur.execute("delete from users where userid > '7';")
# conn.commit()
# cur.execute("select * from users where userid > '7'")
# print(cur.fetchall(), sep='\n')

cur.execute("select * from users")
print(*cur.fetchall(), sep='\n')

# cur.execute("delete from orders where orderid > '6';")
# conn.commit()
# cur.execute("select * from orders where orderid > '6'")
# print(cur.fetchall(), sep='\n')

cur.execute("select * from orders")
print(*cur.fetchall(), sep='\n')

# order = ('00007', '2020-01-13', '00008', '777')
# cur.execute("INSERT INTO orders VALUES(?, ?, ?, ?);", order)
# conn.commit()

cur.execute("SELECT users.fname, users.gender FROM users LEFT JOIN orders where users.userid=orders.userid;")
print(cur.fetchall())


