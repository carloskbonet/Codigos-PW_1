
CREATE TABLE IF NOT EXISTS Produtos (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(64) NOT NULL,
    preco FLOAT NOT NULL,
    quantidade INTEGER NOT NULL
);

INSERT INTO Produtos (nome, preco, quantidade) VALUES ('TV Samsung 50pol 4k' , 2999.99 , 43);
INSERT INTO Produtos (nome, preco, quantidade) VALUES ('TV Philco 32pol FullHD' , 2999.99 , 109);
INSERT INTO Produtos (nome, preco, quantidade) VALUES ('TV Samsung 100pol 4k' , 8999.99 , 12);
INSERT INTO Produtos (nome, preco, quantidade) VALUES ('TV Panasonic 64pol 4k' , 3999.99 , 57);
INSERT INTO Produtos (nome, preco, quantidade) VALUES ('TV Sony 34pol 4k' , 3499.99 , 21);

UPDATE Produtos SET preco = 7999.99 WHERE id = 3;


DELETE FROM Produtos WHERE id = 2;

INSERT INTO Produtos (nome, preco, quantidade) VALUES ('TV Fiat 22pol FullHD' , 999.99 , 109);
