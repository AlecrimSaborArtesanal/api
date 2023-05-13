from flask import jsonify, request


################################### ROTAS DE FICHA TECNICA ###################################

# Todos os itens do ficha_tecnica


def get_ficha_tecnica(cursor):
    cursor.execute("SELECT * FROM ficha_tecnica")
    result = cursor.fetchall()
    return jsonify(result)

# Item do ficha_tecnica por id


def get_by_id_ficha_tecnica(cursor, id):
    cursor.execute("SELECT * FROM ficha_tecnica WHERE id = %s", id)
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)

# Adicionar item em ficha_tecnica


def post_ficha_tecnica(db, cursor):
    data = request.get_json()
    cursor.execute("INSERT INTO ficha_tecnica (id_estoque, id_cardapio, id_lote, obs_item, descricao, quantidade, tempo_preparo) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                   (data['id_estoque'], data['id_cardapio'], data['id_lote'], data['obs_item'], data['descricao'], data['quantidade'], data['tempo_preparo'],))
    db.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso a ficha_tecnica'})


# Atualizar item em ficha_tecnica


def edit_by_id_ficha_tecnica(db, cursor, id):
    data = request.get_json()
    cursor.execute("UPDATE ficha_tecnica SET id_estoque=%s, id_cardapio=%s, id_lote=%s,obs_item=%s, descricao=%s, quantidade=%s, tempo_preparo=%s",
                   ({data['id_estoque'], data['id_cardapio'], data['id_lote'], data['obs_item'], data['descricao'], data['quantidade'], data['tempo_preparo'], id}))
    db.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item das ficha_tecnica


def delete_by_id_ficha_tecnica(db, cursor, id):
    cursor.execute("DELETE FROM ficha_tecnica WHERE id = %s", (id,))
    db.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})
