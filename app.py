from flask import Flask, request, jsonify
import mysql.connector

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

# Todos itens do cardapio


@app.route('/cardapio', methods=['GET'])
def get_cardapio():
    cursor.execute("SELECT * FROM cardapio")
    result = cursor.fetchall()
    return jsonify(result)

# Item do cardapio por id


@app.route('/cardapio/<int:id>', methods=['GET'])
def get_by_id_cardapio(id):
    cursor.execute("SELECT * FROM cardapio WHERE id = %s", (id,))
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)

# Adicionar item no cardapio


@app.route('/cardapio', methods=['POST'])
def post_cardapio():
    data = request.get_json()
    cursor.execute("INSERT INTO cardapio (id, nome, categoria) VALUES (%s, %s, %s)",
                   (data['id'], data['nome'], data['categoria']))
    mydb.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso ao cardápio'})


# Atualizar um item do cardapio

@app.route('/cardapio/<int:id>', methods=['PUT'])
def edit_by_id_cardapio(id):
    data = request.get_json()
    cursor.execute("UPDATE cardapio SET id=%s, nome=%s, categoria=%s WHERE id=%s",
                   (data['id'], data['nome'], data['categoria'], id))
    mydb.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item do cardapio


@app.route('/cardapio/<int:id>', methods=['DELETE'])
def delete_by_id_cardapio(id):
    cursor.execute("DELETE FROM cardapio WHERE id = %s", (id,))
    mydb.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})


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

# Item do estoque por id


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
    return jsonify({'mensagem': 'Registro adicionado com sucesso ao estoque'})

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


# Iniciando aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)
