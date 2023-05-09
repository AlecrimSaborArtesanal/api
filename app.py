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
def tabela_cardapio():
    cursor.execute("SELECT * FROM cardapio")
    resultado = cursor.fetchall()
    return jsonify(resultado)

# Item do cardapio por id


@app.route('/cardapio/<int:id>', methods=['GET'])
def tabela_cardapio_item(id):
    cursor.execute("SELECT * FROM cardapio WHERE id = %s", (id,))
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)

# Adicionar item no cardapio


@app.route('/cardapio', methods=['POST'])
def tabela_cardapio_adicionar_item():
    data = request.get_json()
    cursor.execute("INSERT INTO cardapio (id, nome, categoria) VALUES (%s, %s, %s)",
                   (data['id'], data['nome'], data['categoria']))
    mydb.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso ao cardápio'})


# Atualizar um item do cardapio

@app.route('/cardapio/<int:id>', methods=['PUT'])
def tabala_cardapio_atualizar_item(id):
    data = request.get_json()
    cursor.execute("UPDATE cardapio SET id=%s, nome=%s, categoria=%s WHERE id=%s",
                   (data['id'], data['nome'], data['categoria'], id))
    mydb.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item do cardapio


@app.route('/cardapio/<int:id>', methods=['DELETE'])
def tabala_cardapio_excluir_item(id):
    cursor.execute("DELETE FROM cardapio WHERE id = %s", (id,))
    mydb.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})


################################### ROTAS DE CAIXA ###################################

# Todos itens do caixa

@app.route('/caixa', methods=['GET'])
def tabela_caixa():
    cursor.execute("SELECT * FROM caixa")
    resultado = cursor.fetchall()
    return jsonify(resultado)

# Item do caixa por id


@app.route('/caixa/<int:id>', methods=['GET'])
def tabela_caixa_item(id):
    cursor.execute("SELECT * FROM caixa WHERE id = %s", (id,))
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)

# Adicionar item no caixa


@app.route('/caixa', methods=['POST'])
def tabela_caixa_adicionar_item():
    data = request.get_json()
    cursor.execute("INSERT INTO caixa (id, operacao) VALUES (%s, %s)",
                   (data['id'], data['operacao'],))
    mydb.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso ao caixa'})

# Atualizar um item do caixa


@app.route('/caixa/<int:id>', methods=['PUT'])
def tabala_caixa_atualizar_item(id):
    data = request.get_json()
    cursor.execute("UPDATE caixa SET id=%s, operacao=%s,",
                   (data['id'], data['operacao'], id))
    mydb.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item do caixa


@app.route('/caixa/<int:id>', methods=['DELETE'])
def tabala_caixa_excluir_item(id):
    cursor.execute("DELETE FROM caixa WHERE id = %s", (id,))
    mydb.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})


################################### ROTAS DE VENDAS ###################################

# Todos itens do vendas

@app.route('/vendas', methods=['GET'])
def tabela_vendas():
    cursor.execute("SELECT * FROM vendas")
    resultado = cursor.fetchall()
    return jsonify(resultado)

# Item de vendas por id


@app.route('/vendas/<int:id>', methods=['GET'])
def tabela_vendas_item(id):
    cursor.execute("SELECT * FROM vendas WHERE id = %s", (id,))
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)

# Adicionar item em vendas


@app.route('/vendas', methods=['POST'])
def tabela_vendas_adicionar_item():
    data = request.get_json()
    cursor.execute("INSERT INTO vendas (id, id_caixa) VALUES (%s, %s)",
                   (data['id'], data['id_caixa'],))
    mydb.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso ao vendas'})

# Atualizar um item das vendas


@app.route('/vendas/<int:id>', methods=['PUT'])
def tabala_vendas_atualizar_item(id):
    data = request.get_json()
    cursor.execute("UPDATE vendas SET id=%s, id_caixa=%s,",
                   ({data['id'], data['id_caixa'], id}))
    mydb.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item das vendas


@app.route('/vendas/<int:id>', methods=['DELETE'])
def tabala_vendas_excluir_item(id):
    cursor.execute("DELETE FROM vendas WHERE id = %s", (id,))
    mydb.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})


# Iniciando aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)
