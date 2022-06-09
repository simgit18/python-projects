import sqlite3


def create():
    conn = sqlite3.connect("Database_manipulation/data.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


def insert(item, quant, price):
    conn = sqlite3.connect("Database_manipulation/data.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(?,?,?)", (item, quant, price))
    conn.commit()
    conn.close()


def delete(item):
    conn = sqlite3.connect("Database_manipulation/data.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    conn.commit()
    conn.close()


def update(quant, price, item):
    conn = sqlite3.connect("Database_manipulation/data.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",
                (quant, price, item))
    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("Database_manipulation/data.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    row = cur.fetchall()
    conn.close()

    return row


update(12, 60, 'ball')
print(view())
