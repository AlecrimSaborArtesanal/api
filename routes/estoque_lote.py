from flask import jsonify, request

################################### ROTAS DE ESTOQUE LOTE PROCESSADO ###################################

# Todos os itens do estoque_lote


def get_estoque_lote(cursor):
    cursor.execute("SELECT * FROM estoque_lote_processado")
    result = cursor.fetchall()
    return jsonify(result)

# Item do estoque_lote por id


def get_by_id_estoque_lote(cursor, id):
    cursor.execute("SELECT * FROM estoque_lote_processado WHERE id = %s", id)
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)

# Adicionar item em estoque_lote


def post_estoque_lote(db, cursor):
    data = request.get_json()
    cursor.execute("INSERT INTO estoque_lote_processado (id, nome, quantidade) VALUES (%s, %s, %s)",
                   (data['id'], data['nome'], data['quantidade'],))
    db.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso ao estoque_lote_processado'})

# Atualizar item em estoque_lote


def edit_by_id_estoque_lote(db, cursor, id):
    data = request.get_json()
    cursor.execute("UPDATE estoque_lote_processado SET id=%s, nome=%s, quantidade=%s",
                   ({data['id'], data['nome'], data['quantidade'], id}))
    db.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})


# Excluir um item das estoque_lote


def delete_by_id_estoque_lote(db, cursor, id):
    cursor.execute("DELETE FROM estoque_lote_processado WHERE id = %s", (id,))
    db.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})
