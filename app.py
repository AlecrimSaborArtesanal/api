from flask import Flask, request, jsonify
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="alecrim"
    )
    print('Conexão com banco de dados bem sucedida.')
except:
    print('Conexão com banco de dados não sucedida.')

app = Flask(__name__)


cursor = mydb.cursor()

# rotas de cardapio

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
    cursor.execute("INSERT INTO cardapio (id_produto, nome_produto, descricao_prato, preco_venda, categoria) VALUES (%s, %s, %s, %s, %s)",
                   (data['id_produto'], data['nome_produto'], data['descricao_prato'], data['preco_venda'], data['categoria']))
    mydb.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso ao cardápio'})


# Atualizar um item do cardapio
@app.route('/cardapio/<int:id_produto>', methods=['PUT'])
def tabala_cardapio_atualizar_item(id_produto):
    data = request.get_json()
    cursor.execute("UPDATE cardapio SET id_produto=%s, nome_produto=%s, descricao_prato=%s, preco_venda=%s, categoria=%s WHERE id=%s",
                   (data['id_produto'], data['nome_produto'], data['descricao_prato'], data['preco_venda'], data['categoria'], id_produto))
    mydb.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item do cardapio


@app.route('/cardapio/<int:id_produto>', methods=['DELETE'])
def tabala_cardapio_excluir_item(id_produto):
    cursor.execute("DELETE FROM cardapio WHERE id_produto = %s", (id_produto,))
    mydb.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})


# rotas de clientes

@app.route('/clientes')
def tabela_clientes():
    cursor.execute("SELECT * FROM clientes")
    resultado = cursor.fetchall()
    return jsonify(resultado)


# Iniciando aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)
