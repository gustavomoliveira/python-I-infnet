from conectar_db import *

def consultar_contas_db():
    comando = 'select * from contas;'
    contas = []
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(comando)
    registros = cursor.fetchall()
    for registro in registros:
        conta = Conta(registro[0], registro[1], registro[2])
        contas.append(conta)
    return contas
