import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    database='Professores',
    user='root',
    password=''
)

cursor = conexao.cursor()
cursor.execute('select database();')
cursor.fetchone()