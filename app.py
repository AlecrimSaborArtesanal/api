from flask import Flask, request, jsonify
import mysql.connector
from routes.cardapio import delete_by_id_cardapio, edit_by_id_cardapio, get_cardapio, get_by_id_cardapio, post_cardapio

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="alecrim_normalized"
    )
    print('~*~*~*~*~*~*~*~* Conexão com banco de dados bem sucedida. ~*~*~*~*~*~*~*~*~*')
except:
    print('ERRO! Conexão com banco de dados não sucedida.')

app = Flask(__name__)


cursor = mydb.cursor()

################################### ROTAS DE CARDAPIO ###################################

# GET ALL


@app.route('/cardapio', methods=['GET'])
def get_cardapio_route():
    return get_cardapio(cursor)

# GET BY ID


@app.route('/cardapio/<int:id>', methods=['GET'])
def get_by_id_cardapio_route(id):
    return get_by_id_cardapio(cursor, id)

# POST


@app.route('/cardapio', methods=['POST'])
def post_cardapio_route():
    return post_cardapio(mydb, cursor)

# PUT


@app.route('/cardapio/<int:id>', methods=['PUT'])
def edit_by_id_cardapio_route(id):
    return edit_by_id_cardapio(mydb, cursor, id)

# DELETE


@app.route('/cardapio/<int:id>', methods=['DELETE'])
def delete_by_id_cardapio_route(id):
    return delete_by_id_cardapio(mydb, cursor, id)


################################### ROTAS DE CAIXA ###################################

# Todos itens do caixa

@app.route('/caixa', methods=['GET'])
def get_caixa():
    cursor.execute("SELECT * FROM caixa")
    result = cursor.fetchall()
    return jsonify(result)

# Item do caixa por id


@app.route('/caixa/<int:id>', methods=['GET'])
def get_by_id_caixa(id):
    cursor.execute("SELECT * FROM caixa WHERE id = %s", (id,))
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)

# Adicionar item no caixa


@app.route('/caixa', methods=['POST'])
def post_caixa():
    data = request.get_json()
    cursor.execute("INSERT INTO caixa (id, operacao) VALUES (%s, %s)",
                   (data['id'], data['operacao'],))
    mydb.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso ao caixa'})

# Atualizar um item do caixa


@app.route('/caixa/<int:id>', methods=['PUT'])
def edit_by_id_caixa(id):
    data = request.get_json()
    cursor.execute("UPDATE caixa SET id=%s, operacao=%s,",
                   (data['id'], data['operacao'], id))
    mydb.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item do caixa


@app.route('/caixa/<int:id>', methods=['DELETE'])
def delete_by_id_caixa(id):
    cursor.execute("DELETE FROM caixa WHERE id = %s", (id,))
    mydb.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})


################################### ROTAS DE VENDAS ###################################

# Todos itens do vendas

@app.route('/vendas', methods=['GET'])
def get_vendas():
    cursor.execute("SELECT * FROM vendas")
    result = cursor.fetchall()
    return jsonify(result)

# Item de vendas por id


@app.route('/vendas/<int:id>', methods=['GET'])
def get_by_id_vendas(id):
    cursor.execute("SELECT * FROM vendas WHERE id = %s", (id,))
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)

# Adicionar item em vendas


@app.route('/vendas', methods=['POST'])
def post_vendas():
    data = request.get_json()
    cursor.execute("INSERT INTO vendas (id, id_caixa) VALUES (%s, %s)",
                   (data['id'], data['id_caixa'],))
    mydb.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso a vendas'})

# Atualizar um item das vendas


@app.route('/vendas/<int:id>', methods=['PUT'])
def edit_by_id_vendas(id):
    data = request.get_json()
    cursor.execute("UPDATE vendas SET id=%s, id_caixa=%s,",
                   ({data['id'], data['id_caixa'], id}))
    mydb.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item das vendas


@app.route('/vendas/<int:id>', methods=['DELETE'])
def delete_by_id_vendas(id):
    cursor.execute("DELETE FROM vendas WHERE id = %s", (id,))
    mydb.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})

################################### ROTAS DE ESTOQUE ###################################

# Todos os itens do estoque


@app.route('/estoque', methods=['GET'])
def get_estoque():
    cursor.execute("SELECT * FROM estoque")
    result = cursor.fetchall()
    return jsonify(result)

# Item do estoque por id


@app.route('/estoque/<int:id>', methods=['GET'])
def get_by_id_estoque(id):
    cursor.execute("SELECT * FROM estoque WHERE id = %s", id)
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)

# Adicionar item em estoque


@app.route('/estoque', methods=['POST'])
def post_estoque():
    data = request.get_json()
    cursor.execute("INSERT INTO estoque (id, nome, quantidade, unidade) VALUES (%s, %s, %s, %s)",
                   (data['id'], data['nome'], data['quantidade'], data['unidade'],))
    mydb.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso ao estoque'})

# Atualizar item em estoque


@app.route('/estoque/<int:id>', methods=['PUT'])
def edit_by_id_estoque(id):
    data = request.get_json()
    cursor.execute("UPDATE estoque SET id=%s, nome=%s, quantidade=%s, unidade=%s",
                   ({data['id'], data['nome'], data['quantidade'], data['unidade'], id}))
    mydb.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item das estoque


@app.route('/estoque/<int:id>', methods=['DELETE'])
def delete_by_id_estoque(id):
    cursor.execute("DELETE FROM estoque WHERE id = %s", (id,))
    mydb.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})

################################### ROTAS DE ESTOQUE LOTE PROCESSADO ###################################

# Todos os itens do estoque_lote


@app.route('/estoque_lote', methods=['GET'])
def get_estoque_lote():
    cursor.execute("SELECT * FROM estoque_lote_processado")
    result = cursor.fetchall()
    return jsonify(result)

# Item do estoque_lote por id


@app.route('/estoque_lote/<int:id>', methods=['GET'])
def get_by_id_estoque_lote(id):
    cursor.execute("SELECT * FROM estoque_lote_processado WHERE id = %s", id)
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)

# Adicionar item em estoque_lote


@app.route('/estoque_lote', methods=['POST'])
def post_estoque_lote():
    data = request.get_json()
    cursor.execute("INSERT INTO estoque_lote_processado (id, nome, quantidade) VALUES (%s, %s, %s)",
                   (data['id'], data['nome'], data['quantidade'],))
    mydb.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso ao estoque_lote_processado'})

# Atualizar item em estoque_lote


@app.route('/estoque_lote/<int:id>', methods=['PUT'])
def edit_by_id_estoque_lote(id):
    data = request.get_json()
    cursor.execute("UPDATE estoque_lote_processado SET id=%s, nome=%s, quantidade=%s",
                   ({data['id'], data['nome'], data['quantidade'], id}))
    mydb.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})


# Excluir um item das estoque_lote


@app.route('/estoque_lote/<int:id>', methods=['DELETE'])
def delete_by_id_estoque_lote(id):
    cursor.execute("DELETE FROM estoque_lote_processado WHERE id = %s", (id,))
    mydb.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})


################################### ROTAS DE COMPRAS ###################################

# Todos os itens de compras


@app.route('/compras', methods=['GET'])
def get_compras():
    cursor.execute("SELECT * FROM compras")
    result = cursor.fetchall()
    return jsonify(result)

# Item de compras por id


@app.route('/compras/<int:id>', methods=['GET'])
def get_by_id_compras(id):
    cursor.execute("SELECT * FROM compras WHERE id = %s", id)
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)

# Adicionar item em compras


@app.route('/compras', methods=['POST'])
def post_compras():
    data = request.get_json()
    cursor.execute("INSERT INTO compras (id, data, id_caixa, prazo, forma_pagamento) VALUES (%s, %s, %s, %s, %s)",
                   (data['id'], data['data'], data['id_caixa'], data['prazo'], data['forma_pagamento'],))
    mydb.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso à compras'})

# Atualizar item em compras


@app.route('/compras/<int:id>', methods=['PUT'])
def edit_by_id_compras(id):
    data = request.get_json()
    cursor.execute("UPDATE compras SET id=%s, data=%s, id_caixa=%s, forma_pagamento=%s",
                   ({data['id'], data['data'], data['id_caixa'], data['prazo'], data['forma_pagamento'], id}))
    mydb.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item das compras


@app.route('/compras/<int:id>', methods=['DELETE'])
def delete_by_id_compras(id):
    cursor.execute("DELETE FROM compras WHERE id = %s", (id,))
    mydb.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})


################################### ROTAS DE COMPRAS ITENS ###################################

# Todos os itens de compras_itens


@app.route('/compras_itens', methods=['GET'])
def get_compras_itens():
    cursor.execute("SELECT * FROM compras_itens")
    result = cursor.fetchall()
    return jsonify(result)

# Item do compras_itens por id


@app.route('/compras_itens/<int:id>', methods=['GET'])
def get_by_id_compras_itens(id):
    cursor.execute("SELECT * FROM compras_itens WHERE id = %s", id)
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)


# Adicionar item em compras_itens


@app.route('/compras_itens', methods=['POST'])
def post_compras_itens():
    data = request.get_json()
    cursor.execute("INSERT INTO compras_itens (id_compra, id_estoque, quantidade, custo_unitario) VALUES (%s, %s, %s, %s)",
                   (data['id_compra'], data['id_estoque'], data['quantidade'], data['custo_unitario'],))
    mydb.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso a compras_itens'})


# Atualizar item em compras_itens


@app.route('/compras_itens/<int:id>', methods=['PUT'])
def edit_by_id_compras_itens(id):
    data = request.get_json()
    cursor.execute("UPDATE compras_itens SET id_compra=%s, id_estoque=%s, quantidade=%s, custo_unitario=%s",
                   ({data['id_compra'], data['id_estoque'], data['quantidade'], data['custo_unitario'], id}))
    mydb.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item das compras_itens


@app.route('/compras_itens/<int:id>', methods=['DELETE'])
def delete_by_id_compras_itens(id):
    cursor.execute("DELETE FROM compras_itens WHERE id = %s", (id,))
    mydb.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})


################################### ROTAS DE FICHA TECNICA ###################################

# Todos os itens do ficha_tecnica


@app.route('/ficha_tecnica', methods=['GET'])
def get_ficha_tecnica():
    cursor.execute("SELECT * FROM ficha_tecnica")
    result = cursor.fetchall()
    return jsonify(result)

# Item do ficha_tecnica por id


@app.route('/ficha_tecnica/<int:id>', methods=['GET'])
def get_by_id_ficha_tecnica(id):
    cursor.execute("SELECT * FROM ficha_tecnica WHERE id = %s", id)
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)

# Adicionar item em ficha_tecnica


@app.route('/ficha_tecnica', methods=['POST'])
def post_ficha_tecnica():
    data = request.get_json()
    cursor.execute("INSERT INTO ficha_tecnica (id_estoque, id_cardapio, id_lote, obs_item, descricao, quantidade, tempo_preparo) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (data['id_estoque'], data['id_cardapio'], data['id_lote'], data['obs_item'], data['descricao'], data['quantidade'], data['tempo_preparo'],))
    mydb.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso a ficha_tecnica'})


# Atualizar item em ficha_tecnica


@app.route('/ficha_tecnica/<int:id>', methods=['PUT'])
def edit_by_id_ficha_tecnica(id):
    data = request.get_json()
    cursor.execute("UPDATE ficha_tecnica SET id_estoque=%s, id_cardapio=%s, id_lote=%s,obs_item=%s, descricao=%s, quantidade=%s, tempo_preparo=%s",
                   ({data['id_estoque'], data['id_cardapio'], data['id_lote'], data['obs_item'], data['descricao'], data['quantidade'], data['tempo_preparo'], id}))
    mydb.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item das estoque


@app.route('/ficha_tecnica/<int:id>', methods=['DELETE'])
def delete_by_id_ficha_tecnica(id):
    cursor.execute("DELETE FROM ficha_tecnica WHERE id = %s", (id,))
    mydb.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})


################################### ROTAS DE VENDAS PRODUTOS ###################################

# Todos os itens do vendas_produto


@app.route('/vendas_produto', methods=['GET'])
def get_vendas_produto():
    cursor.execute("SELECT * FROM vendas_produto")
    result = cursor.fetchall()
    return jsonify(result)

# Item do vendas_produto por id


@app.route('/vendas_produto/<int:id>', methods=['GET'])
def get_by_id_vendas_produto(id):
    cursor.execute("SELECT * FROM vendas_produto WHERE id = %s", id)
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)


# Adicionar item em vendas_produto


@app.route('/vendas_produto', methods=['POST'])
def post_vendas_produto():
    data = request.get_json()
    cursor.execute("INSERT INTO vendas_produto (id_venda, id_cardapio, quantidade, forma_pagamento, hora, data) VALUES (%s, %s, %s, %s, %s, %s)",
                   (data['id_venda'], data['id_cardapio'], data['quantidade'], data['forma_pagamento'], data['hora'], data['data'],))
    mydb.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso ao vendas_produto'})

# Atualizar item em vendas_produto


@app.route('/vendas_produto/<int:id>', methods=['PUT'])
def edit_by_id_vendas_produto(id):
    data = request.get_json()
    cursor.execute("UPDATE vendas_produto SET id_venda=%s, id_cardapio=%s, quantidade=%s, forma_pagamento=%s, hora=%s, data=%s",
                   ({data['id_venda'], data['id_cardapio'], data['quantidade'], data['forma_pagamento'], data['hora'], data['data'], id}))
    mydb.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item das vendas_produto


@app.route('/vendas_produto/<int:id>', methods=['DELETE'])
def delete_by_id_vendas_produto(id):
    cursor.execute("DELETE FROM vendas_produto WHERE id = %s", (id,))
    mydb.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})

################################### ROTAS DE FICHA TECNICA LOTE PROCESSADO ###################################

# Todos os itens do ficha_tecnica_lote


@app.route('/ficha_tecnica_lote', methods=['GET'])
def get_ficha_tecnica_lote():
    cursor.execute("SELECT * FROM ficha_tecnica_lote_processado")
    result = cursor.fetchall()
    return jsonify(result)


# Item do ficha_tecnica_lote por id


@app.route('/ficha_tecnica_lote/<int:id>', methods=['GET'])
def get_by_id_ficha_tecnica_lote(id):
    cursor.execute(
        "SELECT * FROM ficha_tecnica_lote_processado WHERE id = %s", id)
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)


# Adicionar item em ficha_tecnica_lote


@app.route('/ficha_tecnica_lote', methods=['POST'])
def post_ficha_tecnica_lote():
    data = request.get_json()
    cursor.execute("INSERT INTO ficha_tecnica_lote_processado (id_estoque, id_lote, rendimento, obs_item, quantidade, tempo_preparo) VALUES (%s, %s, %s, %s, %s, %s)",
                   (data['id_estoque'], data['id_lote'], data['rendimento'], data['obs_item'], data['quantidade'], data['tempo_preparo'],))
    mydb.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso ao ficha_tecnica_lote_processado'})


# Atualizar item em ficha_tecnica_lote


@app.route('/ficha_tecnica_lote/<int:id>', methods=['PUT'])
def edit_by_id_ficha_tecnica_lote(id):
    data = request.get_json()
    cursor.execute("UPDATE ficha_tecnica_lote_processado SET id_estoque=%s, id_lote=%s, rendimento=%s, obs_item=%s, quantidade=%s, tempo_preparo=%s",
                   ({data['id_estoque'], data['id_lote'], data['rendimento'], data['obs_item'], data['quantidade'], data['tempo_preparo'], id}))
    mydb.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item das ficha_tecnica_lote


@app.route('/ficha_tecnica_lote/<int:id>', methods=['DELETE'])
def delete_by_id_ficha_tecnica_lote(id):
    cursor.execute(
        "DELETE FROM ficha_tecnica_lote_processado WHERE id = %s", (id,))
    mydb.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})


# Iniciando aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)
