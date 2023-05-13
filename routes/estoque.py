from flask import jsonify, request

################################### ROTAS DE ESTOQUE ###################################

# Todos os itens do estoque


def get_estoque(cursor):
    cursor.execute("SELECT * FROM estoque")
    result = cursor.fetchall()
    return jsonify(result)

# Item do estoque por id


def get_by_id_estoque(cursor, id):
    cursor.execute("SELECT * FROM estoque WHERE id = %s", id)
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)

# Adicionar item em estoque


def post_estoque(db, cursor):
    data = request.get_json()
    cursor.execute("INSERT INTO estoque (id, nome, quantidade, unidade) VALUES (%s, %s, %s, %s)",
                   (data['id'], data['nome'], data['quantidade'], data['unidade'],))
    db.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso ao estoque'})

# Atualizar item em estoque


def edit_by_id_estoque(db, cursor, id):
    data = request.get_json()
    cursor.execute("UPDATE estoque SET id=%s, nome=%s, quantidade=%s, unidade=%s",
                   ({data['id'], data['nome'], data['quantidade'], data['unidade'], id}))
    db.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item das estoque


def delete_by_id_estoque(db, cursor, id):
    cursor.execute("DELETE FROM estoque WHERE id = %s", (id,))
    db.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})
