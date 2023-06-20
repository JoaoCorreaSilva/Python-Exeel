from conectar import conexao, cursor

def up_usuario(idUser, usuario, email, plano, tipo, idade):
    sql = f"""UPDATE usuarios SET usuario='{usuario}', email = '{email}', plano = '{plano}', 
    tipo = '{tipo}', idade = '{idade}' WHERE idUsuario = '{idUser}';"""
    cursor.execute(sql)
    conexao.commit()


