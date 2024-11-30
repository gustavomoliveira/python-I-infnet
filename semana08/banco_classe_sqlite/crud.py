""" CRUD """

# CRUD -> Create, Read, Update, Delete
# gerenciar ID, Nome, Saldo

from util import *
from models import *
from crud_db import *

def consultar_contas():
    contas = consultar_contas_db()
    for conta in contas:
        print(conta) # sem []

def consultar_conta():
    id = entrar_id()
    conta = consultar_conta_db(id)
    if not conta:
        print('ERRO: Conta não existe')
        return
    print(conta)

def incluir_conta():
    nome = entrar_nome()
    saldo = entrar_saldo()
    conta = Conta(None, nome, saldo) # a posição do id está None porque quem gera o id é o próprio banco
    incluir_conta_db(conta)

def excluir_conta():
        id = entrar_id()
        conta = consultar_conta_db(id)
        if not conta:
            print('ERRO: Conta não existe')
            return
        excluir_conta_db(conta)

def entrar_operacao():
    while True:
        operacao = input('[C]Crédito ou [D]Débito: ').upper()
        if operacao not in ('C', 'D'): # pythonic com tratamento de erro
            print('ERRO: Operação inválida.')
        else:
            break
    return operacao

def entrar_valor():
    while True:
        valor = float(input('Entre com o valor: '))
        if valor <= 0:
            print('ERRO: valor inválido.')
        else:
            break
    return valor

def alterar_conta():
    id = entrar_id()
    conta = consultar_conta_db(id)
    if not conta:
        print('ERRO: Conta não existe.')
        return
    operacao = entrar_operacao()
    valor = entrar_valor()
    if operacao == 'c':
        conta.creditar(valor)
    else:
        conta.debitar(valor)
    alterar_conta_db(conta)