from datetime import datetime
from tabulate import tabulate
from validacoes import *

def menu():
    opcao = validar_opcao( 
    '===== Caixa Supermercado =====\n\n'
    f'[1] - Iniciar Atendimento\n'
    f'[2] - Conferir Estoque\n'
    f'[0] - Fechar Caixa\n'
    '\n=============================\n'
    'Escolha uma opção para iniciar: '
    )
    return opcao

def montar_lista_produtos(produtos):
    while True:
        id = validar_id('\nInsira o id do produto a ser adicionado: ', produtos)
        qtde = validar_qtde('\nInsira a quantidade desse produto: ')
        lista_produtos = []

        for produto in produtos:
            if id == produto[0]:
                if produto[2] == 0:
                    print(f'\nO {produto[1]} está fora de estoque e não pode ser adicionado ao carrinho.')
                    break

                qtde_comprada = min(qtde, produto[2])
                valor_total = qtde_comprada * produto[3]
                produto[2] -= qtde_comprada

                if qtde > qtde_comprada:
                    print(f'\nA quantidade solicitada é maior que o estoque disponível.\n'
                    f'O valor foi ajustado para a quantidade máxima em estoque, {qtde_comprada}.\n')

                lista_produtos = [produto[0], produto[1], qtde_comprada, produto[3], valor_total]
                return lista_produtos

def exibir_estoque(produtos):
    print(f'\nCaixa aberto. Lista de produtos disponíveis:\n')
    print(tabulate(produtos, headers=['Id', 'Nome', 'Qtde', 'Preço']))
    print('--------------------------------\n')

def somar_total(cliente):
    soma_total = 0 
    for total in cliente:
        soma_total += total[4]
    return soma_total

def data_hora_atual():
    data_hora_atual = datetime.now()
    data = data_hora_atual.strftime('%d/%m/%Y')
    hora = data_hora_atual.strftime('%H:%M')
    return f'{data} {hora}'