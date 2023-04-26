import mysql.connector

# Cria conexão com o banco de dados
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='alecrim'
)


# Cria tabela clientes
cursor = cnx.cursor()
query = '''
    CREATE TABLE clientes (
        id_cliente INT AUTO_INCREMENT PRIMARY KEY,
        nome_cliente VARCHAR(50) NOT NULL,
        sexo ENUM('M', 'F'),
        nascimento DATE,
        nacionalidade VARCHAR(20) DEFAULT 'Brasil',
        email VARCHAR(50) UNIQUE,
        telefone VARCHAR(15)
    )
'''
cursor.execute(query)

# Cria tabela cardapio
query = '''
    CREATE TABLE cardapio (
        id_produto INT AUTO_INCREMENT PRIMARY KEY,
        nome_produto VARCHAR(50) NOT NULL,
        descricao_prato VARCHAR(200) NOT NULL,
        preco_venda DECIMAL(10, 2) NOT NULL,
        categoria VARCHAR(50) NOT NULL
    )
'''
cursor.execute(query)

# Cria tabela estoque
query = '''
    CREATE TABLE estoque (
        id_item INT AUTO_INCREMENT PRIMARY KEY,
        nome_item VARCHAR(50) NOT NULL,
        quantidade_estoque INT NOT NULL,
        unidade VARCHAR(10) NOT NULL,
        valor_unitario DECIMAL(10, 2) NOT NULL
    )
'''
cursor.execute(query)

# cria tabela estoque_lote_processado
query = '''
    CREATE TABLE estoque_lote_processado (
        id_lote INT NOT NULL PRIMARY KEY,
        nome_lote VARCHAR(50),
        quantidade INT,
        unidade VARCHAR(10) NOT NULL,
        quantidade_lote DECIMAL(8,2) NOT NULL,
        custo_lote DECIMAL(8,2),
        descricao VARCHAR(200)
      
    )
'''
cursor.execute(query)

# Cria tabela compras
query = '''
    CREATE TABLE compras (
        id_compra INT AUTO_INCREMENT PRIMARY KEY,
        data_compra DATE NOT NULL,
        fornecedor VARCHAR(50) NOT NULL
    )
'''
cursor.execute(query)

# Cria tabela compras_itens
query = '''
    CREATE TABLE compras_itens (
        id_compra INT NOT NULL,
        id_item INT NOT NULL,
        nome_item VARCHAR(50),
        quantidade INT,
        unidade VARCHAR(10) NOT NULL,
        preco_unitario DECIMAL(10, 2),
        FOREIGN KEY (id_compra) REFERENCES compras(id_compra),
        FOREIGN KEY (id_item) REFERENCES estoque(id_item),
        PRIMARY KEY (id_compra, id_item)
    )
'''
cursor.execute(query)

# Cria tabela ficha_tecnica
query = '''
    CREATE TABLE ficha_tecnica (
        id_item INT,
        id_produto INT NOT NULL,
        id_lote INT,
        nome_produto VARCHAR(50) NOT NULL,
        nome_item VARCHAR(50) NOT NULL,
        nome_lote VARCHAR(50),
        obs_item VARCHAR(50),
        descricao VARCHAR(200) NOT NULL,
        quantidade INT NOT NULL,
        unidade VARCHAR(10) NOT NULL,
        valor_unitario DECIMAL(10, 2) NOT NULL,
        preco_unitario DECIMAL(10, 2) NOT NULL,
        tempo_preparo TIME NOT NULL,
        categoria VARCHAR(50) NOT NULL,
        FOREIGN KEY (id_produto) REFERENCES cardapio(id_produto),
        FOREIGN KEY (id_item) REFERENCES estoque(id_item),
        FOREIGN KEY (id_lote) REFERENCES estoque_lote_processado(id_lote)
    )
'''
cursor.execute(query)


# Cria tabela vendas
query = '''
    CREATE TABLE vendas (
        id_venda INT AUTO_INCREMENT PRIMARY KEY,
        id_cliente INT,
        nome_cliente VARCHAR(50),
        id_produto INT NOT NULL,
        quantidade INT NOT NULL,
        valor_unitario DECIMAL(10, 2) NOT NULL,
        total_venda DECIMAL(10, 2) NOT NULL,
        forma_pagamento VARCHAR(50) NOT NULL,
        hora TIME NOT NULL,
        data DATE NOT NULL,
        FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente),
        FOREIGN KEY (id_produto) REFERENCES cardapio(id_produto)
    )
'''
cursor.execute(query)


# cria tabela ficha_tecnica_lote_processado
query = '''
    CREATE TABLE ficha_tecnica_lote_processado (
        id_item INT NOT NULL,
        id_lote INT NOT NULL,
        nome_item VARCHAR(50),
        obs_item VARCHAR(50),
        nome_lote VARCHAR(50),
        quantidade INT,
        unidade VARCHAR(10) NOT NULL,
        preco_unitario DECIMAL(10,2),
        tempo_preparo TIME NOT NULL,
        FOREIGN KEY (id_lote) REFERENCES estoque_lote_processado(id_lote)
    )
'''
cursor.execute(query)

# fecha conexão
cnx.close()
