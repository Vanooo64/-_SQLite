import sqlite3 as sq

with sq.connect('saper.db') as con: #контекст менеджер відкриває БД, функція connect встановлює звязок з БД
    cur = con.cursor() #виконується робота з БД

    cur.execute("DROP TABLE IF EXISTS users") #видаленння таблоиці
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY ,
    name TEXT NOT NULL DEFAULT 1,
    sex INTEGER NOT NULL DEFAULT 1,
    old INTEGER,
    score INTEGER
    )""")# передається SQL запит до БД


