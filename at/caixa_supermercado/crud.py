from validacoes import *
from utilitarios import *
from tabulate import tabulate

def iniciar_atendimento(produtos, proximo_cliente_id):
    cliente = []
    soma_total = 0
    print(f'\nIniciando atendimento para o Cliente {proximo_cliente_id}')

    while True:
        lista_produtos = montar_lista_produtos(produtos)
        if lista_produtos:
            soma_total += lista_produtos[4]
            cliente.append(lista_produtos)
            continuar = validar_entrada('\nDeseja continuar adicionando items?\n'
                                    '\ns - Continuar a Adicionar\n'
                                    '\nn - Finalizar Atendimento\n'
                                    '\nResposta: ')
        if continuar != 's':
            break 
    cliente.append(soma_total)
    finalizar_atendimento(cliente, proximo_cliente_id)
    return cliente, proximo_cliente_id + 1

def finalizar_atendimento(cliente, proximo_cliente_id):
    soma_total = cliente[-1]
    tabela_resumida = []
    colunas_tabela = ['Item', 'Produto', 'Qtde', 'Preço', 'Total']

    print('\n===========================================')
    print(f'\nCliente {proximo_cliente_id}\n')
    print(f'Data: {data_hora_atual()}\n')

    for i, produto in enumerate(cliente[:-1], start=1):
        tabela_resumida.append([i, produto[1], produto[2], produto[3], produto[4]])
 
    print(tabulate(tabela_resumida, headers=colunas_tabela))

    print(f'\nItens: {len(cliente) - 1}')
    print(f'Total: {soma_total}\n')
    print('===========================================\n')

def conferir_estoque(produtos):
    sem_estoque = [produto for produto in produtos if produto[2] == 0]
    
    if sem_estoque:
        print('\nProdutos sem estoque:')
        for produto in sem_estoque:
            print(f'{produto[1]}')
    else:
        print('\nTodos os produtos possuem estoque.\n')
        print('====================================')

def fechar_caixa(clientes, produtos):
    print('\n===== Fechamento do Caixa =====\n')
    print(f'Data: {data_hora_atual()}\n')

    total_de_vendas = 0
    tabela_resumida = []

    for i, cliente in enumerate(clientes, start=1):
        soma_total = cliente[-1]
        tabela_resumida.append([f'Cliente {i}', soma_total])
        total_de_vendas += soma_total 
    
    print(tabulate(tabela_resumida, headers=['Cliente', 'Total']))
    print(f'\nTotal de Vendas: {total_de_vendas}')
    conferir_estoque(produtos)