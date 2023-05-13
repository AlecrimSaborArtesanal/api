from flask import jsonify, request

################################### ROTAS DE CAIXA ###################################

# Todos itens do caixa


def get_caixa(cursor):
    cursor.execute("SELECT * FROM caixa")
    result = cursor.fetchall()
    return jsonify(result)


# Item do caixa por Id


def get_by_id_caixa(cursor, id):
    cursor.execute("SELECT * FROM caixa WHERE id = %s", (id,))
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)


# Acidionar item no caixa


def post_caixa(db, cursor):
    data = request.get_json()
    cursor.execute("INSERT INTO caixa (id, operacao) VALUES (%s, %s)",
                   (data['id'], data['operacao'],))
    db.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso ao caixa'})

# Atualizar um item do caixa


def edit_by_id_caixa(db, cursor, id):
    data = request.get_json()
    cursor.execute("UPDATE caixa SET id=%s, operacao=%s,",
                   (data['id'], data['operacao'], id))
    db.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item do caixa


def delete_by_id_caixa(db, cursor, id):
    cursor.execute("DELETE FROM caixa WHERE id = %s", (id,))
    db.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})
