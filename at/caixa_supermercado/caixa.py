import pathlib
from tabulate import tabulate
from datetime import datetime

DIR_CUR = pathlib.Path(__file__).parent.resolve()
ARQ = str(DIR_CUR) + '/produtos.csv'

def validar_id(msg):
    while True:
        try:
            id = int(input(msg))
            if 1 <= id <= 5:
                return id
            else:
                print('ERRO: Produto não cadastrado. Escolha um id de 1 a 5.')
        except ValueError:
            print('ERRO: Digite um número inteiro para o id.')

def validar_qtde(msg):
    while True:
        try:
            qtde = int(input(msg))
            if qtde > 0:
                return qtde
            else:
                print('ERRO: A quantidade inserida deve ser maior que 0.')
        except ValueError:
            print('ERRO: Digite um número inteiro para a quantidade.')

def validar_opcao(msg):
    while True:
        try:
            opcao = int(input(msg))
            if 0 <= opcao <= 2:
                return opcao
            else:
                print('ERRO: Opção inválida. Escolha entre uma das duas opções de atendimento.')
        except ValueError:
            print('ERRO: Digite entre 0 a 2 para selecionar uma opção.')

def validar_entrada(msg):
    while True:
        entrada = input(msg).strip().lower()
        if entrada == 's' or entrada == 'n':
            return entrada
        else:
            print('ERRO: Digite "s" para sim e "n" para não.')

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

def ler_produtos():
    produtos = []
    try:
        with(open(ARQ, 'r', encoding='UTF-8') as arquivo):
            while linha := arquivo.readline():
                campos = linha.strip('\n').split(',')
                id, nome, qtde, preco = int(campos[0]), campos[1], int(campos[2]), int(campos[3])
                produtos.append([id, nome, qtde, preco])
    except Exception as ex:
        print(f'ERRO: Não foi possível ler a lista de produtos. Detalhes: {ex}')
    print(f'\nCaixa aberto. Lista de produtos disponíveis:\n')
    print(tabulate(produtos, headers=['Id', 'Nome', 'Qtde', 'Preço']))
    print('--------------------------------\n')
    return produtos

def realizar_atendimento(produtos):
    clientes = []
    id_cliente = 1

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
                id_cliente = atender_cliente(produtos, clientes, id_cliente)
            case 2:
                conferir_estoque(produtos)
            case 0:
                fechar_caixa(clientes)
                break
            case _:
                print('ERRO: Opção inválida.')

def atender_cliente(produtos, clientes, id_cliente):
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
                cliente, id_cliente = iniciar_atendimento(produtos, id_cliente)
                clientes.append(cliente)
            case 2:
                if cliente is None or not cliente:
                    print('\nNão há clientes atendidos. Primeiro inicie um atendimento.')
                else:
                    finalizar_atendimento(cliente, id_cliente)
                    cliente = None
            case 0:
                print('\nRetornando ao Menu Inicial.\n')
                return id_cliente
            case _:
                print('ERRO: Opção inválida.')

def iniciar_atendimento(produtos, id_cliente):
    cliente = [] # id, nome, qtde, preço, valor total da compra (preço * qtde)
    print(f'\nIniciando atendimento para o Cliente {id_cliente}')

    while True:
        id = validar_id('\nInsira o id do produto a ser adicionado:')
        qtde = validar_qtde('\nInsira a quantidade desse produto:')
        
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
    finalizar_atendimento(cliente, id_cliente)
    return cliente, id_cliente + 1

def finalizar_atendimento(cliente, id_cliente):
    soma_total = somar_total(cliente)

    print(f'\nCliente {id_cliente}\n')
    print(f'Data: {data_hora_atual()}\n')
    #TODO: Item deve ser um numero incrementável e não o item comprado
    print(tabulate(cliente, headers=['Item', 'Produto', 'Qtde', 'Preço', 'Total']))

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
    print(data_hora_atual())

    total_de_vendas = 0
    
    for i, cliente in enumerate(clientes, start=1):
        print(tabulate(cliente[i], {somar_total(cliente)}, headers=['Cliente', 'Total']))
        total_de_vendas += somar_total(cliente)
    
    print(f'\n=== Total de Vendas: {total_de_vendas} ===\n')


produtos = ler_produtos()
realizar_atendimento(produtos)


