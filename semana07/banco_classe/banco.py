""" Banco """
# SOLID
# LEMBRAR: SRP --> Single Responsability Principle
# DRY --> Dont Repeat Yourself

from crud import *
from menu import *
from util import *
from arquivo import *

# no fundo, uma lista de listas é uma matriz. no caso de 'contas', 4 linhas e 3 colunas

FIM = 0 # objetivo --> o número de saída do loop pode mudar
contas = ler_contas()
opcao = entrar_opcao()
while opcao != FIM: # não precisa do case 0
    match opcao:
        case 1:
            incluir_conta(contas)
        case 2:
            alterar_conta(contas)
        case 3:
            excluir_conta(contas)
        case 4:
            consultar_contas(contas)
        case 5:
            consultar_conta(contas)
        case _:
            print('ERRO: Digite uma opção válida.')
    opcao = entrar_opcao()
gravar_contas(contas)
