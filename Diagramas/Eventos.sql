

CREATE TABLE Palestrante (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(36) NOT NULL,
    especialidade VARCHAR(36) NOT NULL,
    email VARCHAR(36) UNIQUE NOT NULL
);

create TABLE Participante (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(36) NOT NULL,
    email VARCHAR(36) UNIQUE NOT NULL
);

CREATE TABLE Local (
    id INTEGER PRIMARY KEY,
    nome VARCHAR(36),
    localizacao VARCHAR(36) NOT NULL
);

CREATE TABLE Evento (
    id INTEGER PRIMARY KEY,
    titulo VARCHAR(36) NOT NULL,
    dataInicio DATETIME UNIQUE NOT NULL,
    dataFim DATETIME NOT NULL

    idPalestrante INTEGER NOT NULL,
    idLocal INTEGER NOT NULL,
    FOREIGN KEY (idPalestrante) REFERENCES Palestrante(id),
    FOREIGN KEY (idLocal) REFERENCES Local(id),
);

INSERT INTO Evento (titulo, dataInicio, dataFim , idPalestrante , idLocal)
VALUES ( 'Nome do evento' , '2024-06-29 17:30' , '2024-06-29 19:30' , 1 , 1 );



CREATE TABLE Inscricao(
    id INTEGER PRIMARY KEY,
    numRegistro VARCHAR(36) UNIQUE NOT NULL

    idParticipante INTEGER NOT NULL,
    idEvento INTEGER NOT NULL,
    FOREIGN KEY (idParticipante) REFERENCES Participante(id),
    FOREIGN KEY (idEvento) REFERENCES Evento(id)
);

INSERT INTO Inscricao (numRegistro , idParticipante, idEvento) VALUES ( '1817235' , 1 , 20 );
INSERT INTO Inscricao (numRegistro , idParticipante, idEvento) VALUES ( '12715' , 4 , 20 );
INSERT INTO Inscricao (numRegistro , idParticipante, idEvento) VALUES ( '973144' , 11 , 20 );