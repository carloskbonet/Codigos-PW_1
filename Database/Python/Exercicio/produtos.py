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

#connection.close();

def create(name:str , price:float , quantity:int):
    try:
        cursor.execute('INSERT INTO Products (name,price,quantity) VALUES (?,?,?)', (name , price , quantity));
        connection.commit();
    
        return {'code' : 201 , 'message' : 'Product Created'};
    except:
        return {'code': 500 , 'message' : 'Internal Error'};

def findBy():
    pass;

def select():
    try:
        products = [];

        cursor.execute('SELECT name,price,quantity FROM Products');
        products = cursor.fetchall();
        return { 'code': 200 , 'data': products};
    
    except:
        return { 'code': 500 , 'data': 'Internal Error'};

def update():
    pass;

def delete():
    pass;