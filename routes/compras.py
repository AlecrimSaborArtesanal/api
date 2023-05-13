from flask import jsonify, request

################################### ROTAS DE COMPRAS ###################################

# Todos os itens de compras


def get_compras(cursor):
    cursor.execute("SELECT * FROM compras")
    result = cursor.fetchall()
    return jsonify(result)

# Item de compras por id


def get_by_id_compras(cursor, id):
    cursor.execute("SELECT * FROM compras WHERE id = %s", id)
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)

# Adicionar item em compras


def post_compras(db, cursor):
    data = request.get_json()
    cursor.execute("INSERT INTO compras (id, data, id_caixa, prazo, forma_pagamento) VALUES (%s, %s, %s, %s, %s)",
                   (data['id'], data['data'], data['id_caixa'], data['prazo'], data['forma_pagamento'],))
    db.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso à compras'})

# Atualizar item em compras


def edit_by_id_compras(db, cursor, id):
    data = request.get_json()
    cursor.execute("UPDATE compras SET id=%s, data=%s, id_caixa=%s, forma_pagamento=%s",
                   ({data['id'], data['data'], data['id_caixa'], data['prazo'], data['forma_pagamento'], id}))
    db.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item das compras


def delete_by_id_compras(db, cursor, id):
    cursor.execute("DELETE FROM compras WHERE id = %s", (id,))
    db.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})
