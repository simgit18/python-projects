import sqlite3


def connect():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY,title TEXT, Author TEXT, year INTEGER,  Isbn INTEGER)")
    conn.commit()
    conn.close()


connect()


def insert(title, author, year, isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(NULL,?,?,?,?)",
                (title, author, year, isbn))
    conn.commit()
    conn.close()


def delete(id):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()


def update(id, title, author, year, isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?,year=?, isbn=? WHERE id=?",
                (title, author, year, isbn, id))
    conn.commit()
    conn.close()


def search(title="", author="", year="", isbn=""):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn = ?",
                (title, author, year, isbn))
    row = cur.fetchall()
    conn.close()

    return row


def view():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    row = cur.fetchall()
    conn.close()

    return row


print(view())
