""" Funções auxiliares """

# CRUD -> Create, Read, Update, Delete

# gerenciar ID, Nome, Saldo

def entrar_inteiro(txt):
    while True:
        try:
            num = int(input(txt))
            break
        except:
            print('ERRO: Valor inválido.')
    return num

def entrar_id():
    while True:
        id = entrar_inteiro('Entre com o ID da conta: ')
        if id <= 0:
            print('ERRO: ID inválido.')
        else:
            return id

def entrar_nome():
    nome = input('Entre com o nome: ')
    if all(letra.isalpha or letra.isspace for letra in nome):
        return nome
    else:    
        print('Digite apenas letras/caracteres: ')
    
def entrar_saldo():
    while True:
        saldo = float(input('Entre com o saldo da conta: '))
        if saldo < 0:
            print('ERRO: Saldo menor que 0.')
        else:
            return saldo

""" def procurar_conta(contas, id):
    achou = False
    for conta in contas:
        if conta[0] == id:
            achou = True
            break
    return achou """

def procurar_conta(contas, id):
    conta_procurada = [] # se a conta não existe em 'contas', como é uma lista dentro de uma lista, o retorno é uma lista vazia.
    for conta in contas:
        if conta.id == id:
            conta_procurada = conta # significa que uma conta procurada foi encontrada
            break
    return conta_procurada
