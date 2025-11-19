CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    preco DECIMAL(10,2) NOT NULL
);

INSERT INTO produtos (nome, preco) VALUES
('Mouse Gamer', 150.00),
('Teclado Mecânico', 350.00),
('Monitor 27"', 1200.00);

CREATE TABLE controle (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255)
);

INSERT INTO controle (descricao) VALUES
('Primeiro registro'),
('Segundo registro'),
('Terceiro registro');
