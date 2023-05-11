from flask import jsonify, request


################################### ROTAS DE CARDAPIO ###################################

# Todos itens do cardapio


def get_cardapio(cursor):
    cursor.execute("SELECT * FROM cardapio")
    result = cursor.fetchall()
    return jsonify(result)


# Item do cardapio por id


def get_by_id_cardapio(cursor, id):
    cursor.execute("SELECT * FROM cardapio WHERE id = %s", (id,))
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)


# Adicionar item no cardapio


def post_cardapio(db, cursor):
    data = request.get_json()
    cursor.execute("INSERT INTO cardapio (id, nome, categoria) VALUES (%s, %s, %s)",
                   (data['id'], data['nome'], data['categoria']))
    db.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso ao cardápio'})

# Atualizar um item do cardapio


def edit_by_id_cardapio(db, cursor, id):
    data = request.get_json()
    cursor.execute("UPDATE cardapio SET id=%s, nome=%s, categoria=%s WHERE id=%s",
                   (data['id'], data['nome'], data['categoria'], id))
    db.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})


# Excluir um item do cardapio


def delete_by_id_cardapio(db, cursor, id):
    cursor.execute("DELETE FROM cardapio WHERE id = %s", (id,))
    db.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})
