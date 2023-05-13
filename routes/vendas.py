from flask import jsonify, request

################################### ROTAS DE VENDAS ###################################

# Todos itens do vendas


def get_vendas(cursor):
    cursor.execute("SELECT * FROM vendas")
    result = cursor.fetchall()
    return jsonify(result)

# Item de vendas por id


def get_by_id_vendas(cursor, id):
    cursor.execute("SELECT * FROM vendas WHERE id = %s", (id,))
    item = cursor.fetchone()
    if item is None:
        return jsonify({'mensagem': 'Registro não encontrado'}), 404
    return jsonify(item)

# Adicionar item em vendas


def post_vendas(db, cursor):
    data = request.get_json()
    cursor.execute("INSERT INTO vendas (id, id_caixa) VALUES (%s, %s)",
                   (data['id'], data['id_caixa'],))
    db.commit()
    return jsonify({'mensagem': 'Registro adicionado com sucesso a vendas'})

# Atualizar um item das vendas


def edit_by_id_vendas(db, cursor, id):
    data = request.get_json()
    cursor.execute("UPDATE vendas SET id=%s, id_caixa=%s,",
                   ({data['id'], data['id_caixa'], id}))
    db.commit()
    return jsonify({'mensagem': 'Registro atualizado com sucesso'})

# Excluir um item das vendas


def delete_by_id_vendas(db, cursor, id):
    cursor.execute("DELETE FROM vendas WHERE id = %s", (id,))
    db.commit()
    return jsonify({'mensagem': 'Registro excluído com sucesso'})
