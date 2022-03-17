import sqlite3


def seed_db():
    with sqlite3.connect('./db.sqlite3') as conn:
        cursor = conn.cursor()
        sql_file = open("./seed_db.sql")
        sql_as_string = sql_file.read()
        cursor.executescript(sql_as_string)
        print('database ready')
        sql_file.close()

