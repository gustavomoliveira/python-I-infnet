from validacoes import *
from utilitarios import *
from tabulate import tabulate

def realizar_atendimento(produtos):
    clientes = []
    proximo_cliente_id = 1

    while True:
        opcao = validar_opcao(
            '===== Caixa Supermercado =====\n\n'
            f'[1] - Atender Cliente\n'
            f'[2] - Conferir Estoque\n'
            f'[0] - Fechar Caixa\n'
            '\n=============================\n'
            'Escolha uma opção para iniciar: '
        )

        match opcao:
            case 1:
                proximo_cliente_id = atender_cliente(produtos, clientes, proximo_cliente_id)
            case 2:
                conferir_estoque(produtos)
            case 0:
                fechar_caixa(clientes)
                break
            case _:
                print('ERRO: Opção inválida.')

def atender_cliente(produtos, clientes, proximo_cliente_id):
    cliente = None

    while True:
        opcao = validar_opcao(
            '\n===== Atender Cliente =====\n\n'
            f'[1] - Iniciar Atendimento\n'
            f'[2] - Finalizar Atendimento\n'
            f'[0] - Voltar ao Menu Principal\n'
            '\n=============================\n'
            'Escolha uma opção para iniciar: '
        )

        match opcao:
            case 1:
                cliente, proximo_cliente_id = iniciar_atendimento(produtos, proximo_cliente_id)
                clientes.append(cliente)
            case 2:
                if cliente is None or not cliente:
                    print('\nNão há clientes atendidos. Primeiro inicie um atendimento.')
                else:
                    finalizar_atendimento(cliente, proximo_cliente_id)
                    cliente = None
            case 0:
                print('\nRetornando ao Menu Inicial.\n')
                return proximo_cliente_id
            case _:
                print('ERRO: Opção inválida.')

def iniciar_atendimento(produtos, proximo_cliente_id):
    cliente = [] # id, nome, qtde, preço, valor total da compra (preço * qtde)
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
    
    print(cliente)
    finalizar_atendimento(cliente, proximo_cliente_id)
    return cliente, proximo_cliente_id + 1

def finalizar_atendimento(cliente, proximo_cliente_id):
    soma_total = somar_total(cliente)
    tabela_resumida = []
    headers = ['Item', 'Produto', 'Qtde', 'Preço', 'Total']

    print(f'\nCliente {proximo_cliente_id}\n')
    print(f'Data: {data_hora_atual()}\n')

    for i, produto in enumerate(cliente, start=1):
        tabela_resumida.append([
            i, produto[1], produto[2], produto[3], produto[4]
        ])
 
    print(tabulate(tabela_resumida, headers=headers))

    print(f'\nItens: {len(cliente)}')
    print(f'Total: {soma_total}\n')

def conferir_estoque(produtos):
    sem_estoque = False
    
    print('\nProdutos sem estoque:')
    for produto in produtos:
        if produto[2] == 0:
            print(f'\n{produto[1]}')
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