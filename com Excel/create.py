from conecção import conexao, cursor


def inserir_docentes(id, cod, docente, CargaSemanal, gestor):
    inserir_docentes = f"""INSERT INTO professores(id, cod, docente, CargaSemanal, gestor)
    values
    ('{id}', '{cod}', '{docente}', '{CargaSemanal}', '{gestor}');"""
    cursor.execute(inserir_docentes)
    conexao.commit()
