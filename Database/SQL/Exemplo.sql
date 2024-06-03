CREATE TABLE Clientes (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(64) NOT NULL,
    idade INTEGER,
    email VARCHAR(64) NOT NULL
);

-- Para apagar a tabela, use o comando:
DROP TABLE Clientes;


-- Exemplo
--INSERT INTO Clientes (id, nome, idade, email) VALUES (1 ,'Roberto' , 27 , 'troberto.9165@gmail.com');

-- FUNÇÕES DO CRUD

-- C / INSERT
INSERT INTO Clientes (nome, idade, email) VALUES ('Roberto' , 27 , 'troberto.9165@gmail.com');

-- R / SELECT
SELECT * FROM Clientes;
SELECT nome,idade,email FROM Clientes;

-- U / Update
UPDATE Clientes SET idade = 23 WHERE id = 2;
