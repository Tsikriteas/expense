import sqlite3
import datetime
now = datetime.datetime.utcnow()


CREATE_EXPENSES = "CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY,category TEXT, price INTEGER,date DATE);"

CREATE_OTHER = "CREATE TABLE IF NOT EXISTS other (id INTEGER PRIMARY KEY,category TEXT, price INTEGER, date DATE);"

INSERT_EXPENSES = "INSERT INTO expenses (category, price, date) VALUES(?,?,?);"

DELETE_EXPENSES = "DELETE FROM expenses WHERE ID = ?"

DELETE_ALL = "DELETE FROM expenses"

SELECT_ALL = "SELECT * FROM expenses;"

list_db = [CREATE_EXPENSES,CREATE_OTHER]

def create_tables():
    conn = sqlite3.connect('data.db')
    with conn:
        for db in list_db:
            conn.execute(db)
    
def insert_expenses(category,price,date):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(INSERT_EXPENSES, (category,price,date))
        conn.commit()

def select_all_expenses():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(SELECT_ALL)
        list = c.fetchall()
        c.close()
        return list
    
def delete_expense(id):
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_EXPENSES, (id))
        conn.commit()
        c.close()

def delete_all():
    conn = sqlite3.connect('data.db')
    with conn:
        c = conn.cursor()
        c.execute(DELETE_ALL)
        conn.commit()
        c.close()

#create_tables()