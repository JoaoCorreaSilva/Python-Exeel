from conecção import cursor


def listar_usuarios():
    sql = 'SELECT * from usuarios'
    cursor.execute(sql)
    return cursor.fetchall()
