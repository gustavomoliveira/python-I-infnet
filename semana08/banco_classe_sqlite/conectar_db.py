import sqlite3
from models import Conta

BANCO = '/Users/gustavo/Desktop/Infnet/Python I/semana08/banco_classe_sqlite/banco.db'

def conectar():
    try:
        conn = sqlite3.connect(BANCO)
        print('Banco conectado')
    except Exception as ex:
        print(ex)
    return conn

# by default retorna para cada registro do bd uma tupla


