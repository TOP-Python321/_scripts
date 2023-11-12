from pathlib import Path
from pprint import pprint
from sqlite3 import connect, Row
from sys import path


script = '''
drop table if exists auth_group;
drop table if exists auth_group_permissions;
drop table if exists auth_permission;
drop table if exists auth_user;
drop table if exists auth_user_groups;
drop table if exists auth_user_user_permissions;
drop table if exists django_admin_log;
drop table if exists django_content_type;
drop table if exists django_migrations;
drop table if exists django_session;
'''


db_path = Path(path[0]) / 'db.sqlite3'

# создание и настройка объекта подключения
connection = connect(db_path)
# для Python 3.12:
# connection.autocommit = True

# создание объекта курсора
cursor = connection.cursor()

# "размещение" запросов в объект курсора (упаковка запросов в транзакцию) и отправка запроса SQL-движку
cursor.executescript(script)

# подтверждение транзакции
connection.commit()

# запросы выборки в подтверждении не нуждаются
cursor.execute('select * from catalog_book')
pprint(cursor.fetchall())

# [(1, 'Осколки чести', 1),
#  (2, 'Барраяр', 1),
#  (3, 'Спектр', 2),
#  (4, 'Осенние визиты', 2),
#  (5, 'Вино из одуванчиков', 3),
#  (6, 'Электрическое тело, пою', 3)]

# >>> cursor.fetchall()
# []


# использование словароподобных объектов Row для извлечения данных из курсора
cursor.row_factory = Row

cursor.execute('select * from catalog_author')

# без разницы как извлекать данные из курсора
data = []
for row in cursor:
    data.append(row)

# >>> pprint(data)
# [<sqlite3.Row object at 0x0000028828BD1330>,
#  <sqlite3.Row object at 0x0000028828BD1630>,
#  <sqlite3.Row object at 0x0000028828BD16C0>]
# >>>
# >>> data[0].keys()
# ['id', 'first_name', 'last_name']
# >>>
# >>> data[0]['first_name']
# 'Лоис'

# >>> cursor.fetchall()
# []


cursor.row_factory = None

cursor.execute('''
select last_name,
       title
  from catalog_book as b
  join catalog_author as a
    on a.id = b.author_id
''')
pprint(cursor.fetchall())

# [('Буджолд', 'Осколки чести'),
#  ('Буджолд', 'Барраяр'),
#  ('Лукьяненко', 'Спектр'),
#  ('Лукьяненко', 'Осенние визиты'),
#  ('Брэдбери', 'Вино из одуванчиков'),
#  ('Брэдбери', 'Электрическое тело, пою')]

