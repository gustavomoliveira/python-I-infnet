from conectar_db import *
from models import Conta

def incluir_conta_db(conta):
    comando = 'insert into contas (nome, saldo) values (?, ?);'
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando, (conta.nome, conta.saldo))
        conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)

def alterar_conta_db(conta):
    comando = 'update contas set saldo = ? where id = ?;'
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando, (conta.saldo, conta.id))
        conn.commit()
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)

def excluir_conta_db(conta):
    comando = 'delete from contas where id = ?;'
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando, (conta.id,))
        conn.commit() # confirma a operação de exclusão. grava no banco o comando que você solicitou a execução
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)

def consultar_contas_db():
    comando = 'select * from contas;'
    contas = []
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando)
        registros = cursor.fetchall()
        for registro in registros:
            conta = Conta(registro[0], registro[1], registro[2])
            contas.append(conta)
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn) # independente de qualquer coisa o banco é desconectado
    return contas

def consultar_conta_db(id):
    comando = 'select * from contas where id = ?;'
    conta = []
    try:
        conn = conectar()
        cursor = conn.cursor()
        cursor.execute(comando, (id,)) # é necessário colocar a vírgula, mesmo sem o segundo parâmetro, para indicar que esse código é uma tupla
        registro = cursor.fetchall()
        if registro:
            conta = Conta(registro[0][0], registro[0][1], registro[0][2]) # relação linhas e colunas
    except Exception as ex:
        print(ex)
    finally:
        desconectar(conn)
    return conta