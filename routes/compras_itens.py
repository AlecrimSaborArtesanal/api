from flask import jsonify, request

################################### ROTAS DE COMPRAS ITENS ###################################

# Todos os itens de compras_itens


def get_compras_itens(cursor):
    cursor.execute("SELECT * FROM compras_itens")
    result = cursor.fetchall()
    return jsonify(result)

# Item do compras_itens por id


def get_by_id_compras_itens(cursor, id):
    cursor.execute("SELECT * FROM compras_itens WHERE id = %s", id)
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)


# Adicionar item em compras_itens


def post_compras_itens(db, cursor):
    data = request.get_json()
    cursor.execute("INSERT INTO compras_itens (id_compra, id_estoque, quantidade, custo_unitario) VALUES (%s, %s, %s, %s)",
                   (data['id_compra'], data['id_estoque'], data['quantidade'], data['custo_unitario'],))
    db.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso a compras_itens'})


# Atualizar item em compras_itens


def edit_by_id_compras_itens(db, cursor, id):
    data = request.get_json()
    cursor.execute("UPDATE compras_itens SET id_compra=%s, id_estoque=%s, quantidade=%s, custo_unitario=%s",
                   ({data['id_compra'], data['id_estoque'], data['quantidade'], data['custo_unitario'], id}))
    db.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item das compras_itens


def delete_by_id_compras_itens(db, cursor, id):
    cursor.execute("DELETE FROM compras_itens WHERE id = %s", (id,))
    db.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})
