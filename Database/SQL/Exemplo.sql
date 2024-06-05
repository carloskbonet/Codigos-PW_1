CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(64) NOT NULL,
    idade INTEGER,
    email VARCHAR(64) UNIQUE NOT NULL
);

-- Para apagar a tabela, use o comando:
DROP TABLE Clientes;


-- Exemplo
--INSERT INTO Clientes (id, nome, idade, email) VALUES (1 ,'Roberto' , 27 , 'troberto.9165@gmail.com');

-- FUNÇÕES DO CRUD

-- C / INSERT
INSERT INTO Clientes (nome, idade, email) VALUES ('Roberto' , 27 , 'troberto.9165@gmail.com');
INSERT INTO Clientes (nome, idade, email) VALUES ('Ana' , 21 , 'anap1.32@gmail.com');
INSERT INTO Clientes (nome, idade, email) VALUES ('Mauro' , 42 , 'mmiz746@gmail.com');

-- R / SELECT
SELECT * FROM Clientes;
SELECT nome,idade,email FROM Clientes;
SELECT nome,idade,email,Biografia FROM Clientes WHERE email = 'anap1.32@gmail.com';

-- U / Update
UPDATE Clientes SET idade = 20;

UPDATE Clientes SET idade = 27 WHERE id = 1;
UPDATE Clientes SET idade = 22 WHERE id = 2;
UPDATE Clientes SET idade = 42 WHERE id = 3;

-- D / Delete
DELETE FROM Clientes;

DELETE FROM Clientes WHERE id = 1;

-- Alterar Tabela
ALTER TABLE Clientes ADD COLUMN Biografia VARCHAR(300);


