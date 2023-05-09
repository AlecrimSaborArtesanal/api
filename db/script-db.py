import mysql.connector

# Cria conexão com o banco de dados
cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='123456',
    database='alecrim_normalized'
)

# Cria tabela cardapio
cursor = cnx.cursor()

query = '''
    CREATE TABLE cardapio (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        categoria VARCHAR(50) NOT NULL
    )
'''
cursor.execute(query)

# Cria tabela caixa
query = '''
    CREATE TABLE caixa (
        id INT AUTO_INCREMENT PRIMARY KEY,
        operacao VARCHAR(50) NOT NULL
    )
'''
cursor.execute(query)

# Cria tabela vendas
query = '''
    CREATE TABLE vendas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        id_caixa INT,
        FOREIGN KEY (id_caixa) REFERENCES caixa(id)
    )
'''
cursor.execute(query)

# Cria tabela estoque
query = '''
    CREATE TABLE estoque (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nome VARCHAR(50) NOT NULL,
        quantidade INT NOT NULL,
        unidade VARCHAR(10) NOT NULL
    )
'''
cursor.execute(query)

# cria tabela estoque_lote_processado
query = '''
    CREATE TABLE estoque_lote_processado (
        id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
        nome VARCHAR(50),
        quantidade INT
    )
'''
cursor.execute(query)

# Cria tabela compras
query = '''
    CREATE TABLE compras (
        id INT AUTO_INCREMENT PRIMARY KEY,
        data DATE,
        id_caixa INT NOT NULL,
        prazo INT,
        forma_pagamento VARCHAR(50) NOT NULL,
        FOREIGN KEY (id_caixa) REFERENCES caixa(id)
    )
'''
cursor.execute(query)

# Cria tabela compras_itens
query = '''
    CREATE TABLE compras_itens (
        id_compra INT NOT NULL,
        id_estoque INT NOT NULL,
        quantidade INT,
        custo_unitario DECIMAL(10, 2),
        FOREIGN KEY (id_compra) REFERENCES compras(id),
        FOREIGN KEY (id_estoque) REFERENCES estoque(id)
    )
'''
cursor.execute(query)

# Cria tabela ficha_tecnica
query = '''
    CREATE TABLE ficha_tecnica (
        id_estoque INT,
        id_cardapio INT,
        id_lote INT,
        obs_item VARCHAR(50),
        descricao VARCHAR(200),
        quantidade INT NOT NULL,
        tempo_preparo TIME NOT NULL,
        FOREIGN KEY (id_cardapio) REFERENCES cardapio(id),
        FOREIGN KEY (id_estoque) REFERENCES estoque(id),
        FOREIGN KEY (id_lote) REFERENCES estoque_lote_processado(id)
    )
'''
cursor.execute(query)


# Cria tabela vendas produto
query = '''
    CREATE TABLE vendas_produto (
        id_venda INT,
        id_cardapio INT,
        quantidade INT NOT NULL,
        forma_pagamento VARCHAR(50) NOT NULL,
        hora TIME,
        data DATE,
        FOREIGN KEY (id_cardapio) REFERENCES cardapio(id),
        FOREIGN KEY (id_venda) REFERENCES vendas(id)
    )
'''
cursor.execute(query)


# cria tabela ficha_tecnica_lote_processado
query = '''
    CREATE TABLE ficha_tecnica_lote_processado (
        id_estoque INT NOT NULL,
        id_lote INT NOT NULL,
        rendimento VARCHAR(50),
        obs_item VARCHAR(50),
        quantidade INT,
        tempo_preparo TIME NOT NULL,
        FOREIGN KEY (id_lote) REFERENCES estoque_lote_processado(id),
        FOREIGN KEY (id_estoque) REFERENCES estoque(id)
    )
'''
cursor.execute(query)

# fecha conexão
cnx.close()
