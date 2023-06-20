from conecção import conexao, cursor

def up_professores(id, cod, docente, CargaSemanal, gestor):
    sql = f"""UPDATE professores SET docente='{id}', email = '{cod}', plano = '{docente}', 
    tipo = '{CargaSemanal}', idade = '{idade}' WHERE idUsuario = '{idUser}';"""
    cursor.execute(sql)
    conexao.commit()
