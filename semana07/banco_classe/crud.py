""" CRUD """

# CRUD -> Create, Read, Update, Delete
# gerenciar ID, Nome, Saldo

from util import *
from models import *

def consultar_contas(contas):
    for conta in contas:
        print(conta) # sem []

def consultar_conta(contas):
    id = entrar_id()
    conta = procurar_conta(contas, id)
    if not conta:
        print('ERRO: Conta não existe')
        return
    print(conta)

def incluir_conta(contas): # como o parâmetro é uma lista, a passagem é por referência, ou seja, não é necessário retornar o valor.
    id = entrar_id()
    conta = procurar_conta(contas, id)
    if (conta): # o mesmo que --> conta != []
        print('ERRO: Conta já existe.')
        return
    nome = entrar_nome()
    saldo = entrar_saldo()
    incluir_conta = Conta(id, nome, saldo)
    contas.append(incluir_conta)

def excluir_conta(contas):
        id = entrar_id()
        conta = procurar_conta(contas, id)
        if not conta:
            print('ERRO: Conta não existe')
            return
        contas.remove(conta)

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

def alterar_conta(contas):
    id = entrar_id()
    conta = procurar_conta(contas, id)
    if not conta:
        print('ERRO: Conta não existe.')
        return
    operacao = entrar_operacao()
    valor = entrar_valor()
    if operacao == 'c':
        conta.creditar(valor)
    else:
        conta.debitar(valor)