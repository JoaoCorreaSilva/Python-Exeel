from conecção import conexao, cursor


def del_docente(id):
    sql = f"""DELETE FROM professores WHERE id = '{id}';"""
    cursor.execute(sql)
    conexao.commit()