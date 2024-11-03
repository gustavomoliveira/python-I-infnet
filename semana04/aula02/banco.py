# CRUD -> Create, Read, Update, Delete
# gerenciar ID, Nome, Saldo

from util import *

def consultar_contas(contas):
    for conta in contas:
        print(conta[0], conta[1], conta[2]) # sem []

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
    incluir_conta = [id, nome, saldo]
    contas.append(incluir_conta)

def excluir_conta(contas):
        id = entrar_id()
        conta = procurar_conta(contas, id)
        if not conta:
            print('ERRO: Conta não existe')
            return
        contas.remove(conta)

# no fundo, uma lista de listas é uma matriz. no caso de 'contas', 4 linhas e 3 colunas
contas = [
    [1, 'Gustavo', 100],
    [2, 'Mari', 200],
    [3, 'Bartô', 300],
    [4, 'Yoshi', 400]
]

incluir_conta(contas)
consultar_contas(contas)
consultar_conta(contas)
excluir_conta(contas)