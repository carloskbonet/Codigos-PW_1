
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


-- Tabela de Clientes
-- Informações: Nome, CPF, Email, Número, etc . . .
-- Adicionar UNIQUE nas informações que não podem ser repetidas

CREATE TABLE IF NOT EXISTS Clientes (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(64) NOT NULL,
    CPF VARCHAR(18) UNIQUE NOT NULL,
    email VARCHAR(64) UNIQUE NOT NULL,
    numeroContato VARCHAR(18) UNIQUE NOT NULL,
    CEP VARCHAR(18) DEFAULT(''),
    numResidencia VARCHAR(5) DEFAULT('')
);

INSERT INTO Clientes (nome,CPF,email,numeroContato,CEP,numResidencia) VALUES ('Manuel','61982122312','bluepen@gmail.com','88082142','82062103', '921');
INSERT INTO Clientes (nome,CPF,email,numeroContato) VALUES ('Kauan','68385235312','kte211@gmail.com','88028402');
INSERT INTO Clientes (nome,CPF,email,numeroContato) VALUES ('Larissa','11932142659','larshdow@gmail.com','88010421');


-- Tabela de Pedidos
-- Informações: Data do pedido , Quantidade , Valor Final , codigo da compra
-- Adicionar UNIQUE nas informações que não podem ser repetidas e NOT NULL nas informações que não podem ser vazias

CREATE TABLE IF NOT EXISTS Pedidos (
    id INTEGER PRIMARY KEY,
    dataPedido DATE NOT NULL,
    quantidade INTEGER NOT NULL,
    valorFinal FLOAT NOT NULL,
    codigoCompra VARCHAR(18) UNIQUE NOT NULL,
    idCliente INTEGER,
    idProduto INTEGER,
    FOREIGN KEY (idCliente) REFERENCES Clientes(id),
    FOREIGN KEY (idProduto) REFERENCES Produtos(id)
);

INSERT INTO Pedidos(dataPedido,quantidade,valorFinal,codigoCompra,idCliente,idProduto)
VALUES ('2024-06-07' , 2 , 6000 , '123129038213' , 1 , 2);

INSERT INTO Pedidos(dataPedido,quantidade,valorFinal,codigoCompra,idCliente,idProduto)
VALUES ('2024-06-06' , 1 , 2999.99 , '4312466338213' , 2 , 1);