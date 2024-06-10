import sqlite3;

connection = sqlite3.connect('Store.db');
cursor = connection.cursor();

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
        id INTEGER PRIMARY KEY,
        name VARCHAR(32) UNIQUE NOT NULL,
        price FLOAT NOT NULL,
        quantity INTEGER NOT NULL
    );
''');

def create(name:str , price:float , quantity:int):
    cursor.execute('INSERT INTO Products (name,price,quantity) VALUES (?,?,?)', (name , price , quantity));
    connection.commit();

def findBy():
    pass;

def select():
    pass;

def update():
    pass;

def delete():
    pass;