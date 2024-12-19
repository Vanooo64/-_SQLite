import sqlite3 as sq

with sq.connect('saper.db') as con: #контекст менеджер відкриває БД, функція connect встановлює звязок з БД
    cur = con.cursor() #виконується робота з БД

    cur.execute("SELECT * FROM users WHERE score > 200 ORDER BY score DESC LIMIT 5 ")

    # result = cur.fetchall()
    # for i in result:
    #     print(i)

    result = cur.fetchone() # повертає перший запис.
    result2 = cur.fetchmany(2)  #повертає число записів трохи більше size
    print(result)
    print(result2)

