import sqlite3;

command = str('');
result = [];

connection = sqlite3.connect('./Banco.db');
cursor = connection.cursor();

cursor.execute(
    'CREATE TABLE IF NOT EXISTS Produtos (' +
    '   id INTEGER PRIMARY KEY,' +
    '   nome VARCHAR(64) NOT NULL,' +
    '   preco FLOAT NOT NULL,' +
    '   quantidade INTEGER NOT NULL);'
);


cursor.execute('INSERT INTO Produtos (nome, preco, quantidade) VALUES (?,?,?)', ('TV Philco 32pol FullHD' , 2999.99 , 109));
connection.commit();


command = cursor.execute('SELECT * FROM Produtos');
result = command.fetchall();

print(result);