# database.py
import sqlite3

def connect_db():
    conn = sqlite3.connect('sales.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS sales
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT,
                price INTEGER,
                customer_name TEXT)''')
    conn.commit()
    conn.close()

def insert_sale(product, price, customer):
    conn = sqlite3.connect('sales.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO sales (product_name, price, customer_name) VALUES (?, ?, ?)", (product, price, customer))
    conn.commit()
    conn.close()
