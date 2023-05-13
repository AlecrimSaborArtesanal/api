from flask import Flask, request, jsonify
import mysql.connector
from routes.cardapio import delete_by_id_cardapio, edit_by_id_cardapio, get_cardapio, get_by_id_cardapio, post_cardapio
from routes.caixa import delete_by_id_caixa, edit_by_id_caixa, get_caixa, get_by_id_caixa, post_caixa
from routes.vendas import delete_by_id_vendas, edit_by_id_vendas, get_vendas, get_by_id_vendas, post_vendas
from routes.estoque import delete_by_id_estoque, edit_by_id_estoque, get_estoque, get_by_id_estoque, post_estoque
from routes.estoque_lote import delete_by_id_estoque_lote, edit_by_id_estoque_lote, get_estoque_lote, get_by_id_estoque_lote, post_estoque_lote
from routes.compras import delete_by_id_compras, edit_by_id_compras, get_compras, get_by_id_compras, post_compras
from routes.compras_itens import delete_by_id_compras_itens, edit_by_id_compras_itens, get_compras_itens, get_by_id_compras_itens, post_compras_itens
from routes.ficha_tecnica import delete_by_id_ficha_tecnica, edit_by_id_ficha_tecnica, get_ficha_tecnica, get_by_id_ficha_tecnica, post_ficha_tecnica


try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="alecrim_normalized"
    )
    print('~*~*~* [OK] Conexão com banco de dados bem sucedida. *~*~*~')
except:
    print('!!! [ERRO] Conexão com banco de dados não sucedida. !!!')

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

#  GET ALL
@app.route('/caixa', methods=['GET'])
def get_caixa_route():
    return get_caixa(cursor)

# GET BY ID


@app.route('/caixa/<int:id>', methods=['GET'])
def get_by_id_caixa_route(id):
    return get_by_id_caixa(cursor, id)

# POST


@app.route('/caixa', methods=['POST'])
def post_caixa_route():
    return post_caixa(mydb, cursor)

# PUT


@app.route('/caixa/<int:id>', methods=['PUT'])
def edit_by_id_caixa_route(id):
    return edit_by_id_caixa(mydb, cursor, id)

# DELETE


@app.route('/caixa/<int:id>', methods=['DELETE'])
def delete_by_id_caixa_route(id):
    return delete_by_id_caixa(mydb, cursor, id)


################################### ROTAS DE VENDAS ###################################

# GET ALL

@app.route('/vendas', methods=['GET'])
def get_vendas_route():
    return get_vendas(cursor)

# GET BY ID


@app.route('/vendas/<int:id>', methods=['GET'])
def get_by_id_vendas_route(id):
    return get_by_id_vendas(cursor, id)

# POST


@app.route('/vendas', methods=['POST'])
def post_vendas_route():
    return post_vendas(mydb, cursor)

# PUT


@app.route('/vendas/<int:id>', methods=['PUT'])
def edit_by_id_vendas_route(id):
    return edit_by_id_vendas(mydb, cursor, id)

# DELETE


@app.route('/vendas/<int:id>', methods=['DELETE'])
def delete_by_id_vendas_route(id):
    return delete_by_id_vendas(mydb, cursor, id)

################################### ROTAS DE ESTOQUE ###################################

# GET ALL


@app.route('/estoque', methods=['GET'])
def get_estoque_route():
    return get_estoque(cursor)

# GET BY ID


@app.route('/estoque/<int:id>', methods=['GET'])
def get_by_id_estoque_route(id):
    return get_by_id_estoque(cursor, id)

# POST


@app.route('/estoque', methods=['POST'])
def post_estoque_route():
    return post_estoque(mydb, cursor)

# PUT


@app.route('/estoque/<int:id>', methods=['PUT'])
def edit_by_id_estoque_route(id):
    return edit_by_id_estoque(mydb, cursor, id)

# DELETE


@app.route('/estoque/<int:id>', methods=['DELETE'])
def delete_by_id_estoque_route(id):
    return delete_by_id_estoque(mydb, cursor, id)

################################### ROTAS DE ESTOQUE LOTE PROCESSADO ###################################

# GET ALL


@app.route('/estoque_lote', methods=['GET'])
def get_estoque_lote_route():
    return get_estoque_lote(cursor)

# GET BY ID


@app.route('/estoque_lote/<int:id>', methods=['GET'])
def get_by_id_estoque_lote_route(id):
    return get_by_id_estoque_lote(cursor, id)

# POST


@app.route('/estoque_lote', methods=['POST'])
def post_estoque_lote_route():
    return post_estoque_lote(mydb, cursor)

# PUT


@app.route('/estoque_lote/<int:id>', methods=['PUT'])
def edit_by_id_estoque_lote_route(id):
    return edit_by_id_estoque_lote(mydb, cursor, id)


# DELETE


@app.route('/estoque_lote/<int:id>', methods=['DELETE'])
def delete_by_id_estoque_lote_route(id):
    return delete_by_id_estoque_lote(mydb, cursor, id)


################################### ROTAS DE COMPRAS ###################################

# GET ALL

@app.route('/compras', methods=['GET'])
def get_compras_route():
    return get_compras(cursor)

# GET BY ID


@app.route('/compras/<int:id>', methods=['GET'])
def get_by_id_compras_route(id):
    return get_by_id_compras(cursor, id)

# POST


@app.route('/compras', methods=['POST'])
def post_compras_route():
    return post_compras(mydb, cursor)

# PUT


@app.route('/compras/<int:id>', methods=['PUT'])
def edit_by_id_compras_route(id):
    return edit_by_id_compras(mydb, cursor, id)

# DELETE


@app.route('/compras/<int:id>', methods=['DELETE'])
def delete_by_id_compras_route(id):
    return delete_by_id_compras(mydb, cursor, id)


################################### ROTAS DE COMPRAS ITENS ###################################

# GET ALL


@app.route('/compras_itens', methods=['GET'])
def get_compras_itens_route():
    return get_compras_itens(cursor)

# GET BY ID


@app.route('/compras_itens/<int:id>', methods=['GET'])
def get_by_id_compras_itens_route(id):
    return get_by_id_compras_itens(cursor, id)


# POST


@app.route('/compras_itens', methods=['POST'])
def post_compras_itens_route():
    return post_compras_itens(mydb, cursor)


# PUT


@app.route('/compras_itens/<int:id>', methods=['PUT'])
def edit_by_id_compras_itens_route(id):
    return edit_by_id_compras_itens(mydb, cursor, id)

# DELETE


@app.route('/compras_itens/<int:id>', methods=['DELETE'])
def delete_by_id_compras_itens_route(id):
    return delete_by_id_compras_itens(mydb, cursor, id)


################################### ROTAS DE FICHA TECNICA ###################################

# Todos os itens do ficha_tecnica


@app.route('/ficha_tecnica', methods=['GET'])
def get_ficha_tecnica_route():
    return get_ficha_tecnica(cursor)

# Item do ficha_tecnica por id


@app.route('/ficha_tecnica/<int:id>', methods=['GET'])
def get_by_id_ficha_tecnica_route(id):
    return get_by_id_ficha_tecnica(cursor, id)

# Adicionar item em ficha_tecnica


@app.route('/ficha_tecnica', methods=['POST'])
def post_ficha_tecnica_route():
    return post_ficha_tecnica(mydb, cursor)


# Atualizar item em ficha_tecnica


@app.route('/ficha_tecnica/<int:id>', methods=['PUT'])
def edit_by_id_ficha_tecnica_route(id):
    return edit_by_id_ficha_tecnica(mydb, cursor, id)

# Excluir um item das ficha_tecnica


@app.route('/ficha_tecnica/<int:id>', methods=['DELETE'])
def delete_by_id_ficha_tecnica_route(id):
    return delete_by_id_ficha_tecnica(mydb, cursor, id)


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
