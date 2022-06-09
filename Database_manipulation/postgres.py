import psycopg2


def create():
    conn = psycopg2.connect(
        "dbname='db1' user = 'postgres' password='Son@devi1' host='localhost' port = '1804'")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


create()


def insert(item, quant, price):
    conn = psycopg2.connect(
        "dbname='db1' user = 'postgres' password='Son@devi1' host='localhost' port = '1804'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)", (item, quant, price))
    conn.commit()
    conn.close()


def delete(item):
    conn = psycopg2.connect(
        "dbname='db1' user = 'postgres' password='Son@devi1' host='localhost' port = '1804'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    conn.commit()
    conn.close()


def update(quant, price, item):
    conn = psycopg2.connect(
        "dbname='db1' user = 'postgres' password='Son@devi1' host='localhost' port = '1804'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s",
                (quant, price, item))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect(
        "dbname='db1' user = 'postgres' password='Son@devi1' host='localhost' port = '1804'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    row = cur.fetchall()
    conn.close()

    return row


insert('apple', 10, 30)

print(view())
