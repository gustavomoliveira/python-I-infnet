from validacoes import *
from utilitarios import *
from tabulate import tabulate

def iniciar_atendimento(produtos, proximo_cliente_id):
    cliente = []
    print(f'\nIniciando atendimento para o Cliente {proximo_cliente_id}')

    while True:
        id = validar_id('\nInsira o id do produto a ser adicionado: ')
        qtde = validar_qtde('\nInsira a quantidade desse produto: ')
        
        for produto in produtos:
            if id == produto[0]:
                qtde_comprada = min(qtde, produto[2])
                valor_total = qtde_comprada * produto[3]
                produto[2] -= qtde_comprada

                if qtde > qtde_comprada:
                    print(f'A quantidade solicitada é maior que o estoque disponível.\n'
                        f'O valor foi ajustado para a quantidade máxima em estoque, {qtde_comprada}.')

                cliente.append([produto[0], produto[1], qtde_comprada, produto[3], valor_total])
        
        continuar = validar_entrada('\nDeseja continuar adicionando items?\n'
                                    's - Continuar a Adicionar\n'
                                    'n - Finalizar Atendimento\n'
                                    'Resposta: ')
        if continuar != 's':
            break  
    finalizar_atendimento(cliente, proximo_cliente_id)
    return cliente, proximo_cliente_id + 1

def finalizar_atendimento(cliente, proximo_cliente_id):
    soma_total = somar_total(cliente)
    tabela_resumida = []
    colunas_tabela = ['Item', 'Produto', 'Qtde', 'Preço', 'Total']

    print(f'\nCliente {proximo_cliente_id}\n')
    print(f'Data: {data_hora_atual()}\n')

    for i, produto in enumerate(cliente, start=1):
        tabela_resumida.append([
            i, produto[1], produto[2], produto[3], produto[4]
        ])
 
    print(tabulate(tabela_resumida, headers=colunas_tabela))

    print(f'\nItens: {len(cliente)}')
    print(f'Total: {soma_total}\n')

def conferir_estoque(produtos):
    sem_estoque = False
    print('\nProdutos sem estoque:')

    for produto in produtos:
        if produto[2] == 0:
            print(f'{produto[1]}')
            print()
            sem_estoque = True

    if not sem_estoque:
        print('\nTodos os produtos possuem estoque.\n')

def fechar_caixa(clientes):
    print('\n===== Fechamento do Caixa =====\n')
    print(f'Data: {data_hora_atual()}\n')

    total_de_vendas = 0
    tabela_resumida = []

    for i, cliente in enumerate(clientes, start=1):
        soma_total = somar_total(cliente)
        tabela_resumida.append([f'Cliente {i}', soma_total])
        total_de_vendas += soma_total 
    
    print(tabulate(tabela_resumida, headers=['Cliente', 'Total']))
    
    print(f'\n=== Total de Vendas: {total_de_vendas} ===\n')