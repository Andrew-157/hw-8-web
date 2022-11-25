import sqlite3


def connect_db():

    with open('university.sql', 'r') as file:
        sql = file.read()

    with sqlite3.connect('university.db') as con:
        cur = con.cursor()

    cur.executescript(sql)


if __name__ == '__main__':
    connect_db()
