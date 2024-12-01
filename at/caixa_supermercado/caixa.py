import pathlib
from tabulate import tabulate

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

def validar_num_cliente(clientes):
    num_cliente = len(clientes) + 1
    for cliente in clientes:
        if num_cliente == cliente[0]:
            num_cliente += 1
    return num_cliente

def validar_opcao_atendimento(msg):
    while True:
        try:
            opcao = int(input(msg))
            if 1 <= opcao <= 2:
                return opcao
            else:
                print('ERRO: Opção inválida. Escolha entre uma das duas opções de atendimento.')
        except ValueError:
            print('ERRO: Digite 1 ou 2 para selecionar uma opção.')

def validar_entrada(msg):
    while True:
        entrada = input(msg).strip().lower()
        if entrada == 's' or entrada == 'n':
            return entrada
        else:
            print('ERRO: Digite "s" para sim e "n" para não.')

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
    print(f'\nCaixa aberto. Lista de produtos disponíveis:')
    print(produtos[0])
    print(produtos[1])
    print(produtos[2])
    print(produtos[3])
    print(produtos[4])
    return produtos

def atender_cliente(produtos):
    clientes = []
    num = validar_num_cliente(clientes)
    opcao_atendimento = validar_opcao_atendimento(
        f'Cliente {num}:\n'
        f'[1] - Iniciar Atendimendo'
        f'[2] - Finalizar Atendimento'
    )

    if opcao_atendimento == 1:
        clientes.append(iniciar_atendimento(produtos))
    else:
        finalizar_atendimento(clientes)

def iniciar_atendimento(produtos):
    items_cliente = [] # id, nome, qtde, preço, valor total da compra (preço * qtde)

    while True:
        id = validar_id('Insira o id do produto a ser adicionado: ')
        qtde = validar_qtde('Insira a quantidade desse produto: ')
        
        for produto in produtos:
            if id == produto[0]:
                qtde_comprada = min(qtde, produto[2])
                valor_total = qtde_comprada * produto[3]
                produto[2] -= qtde_comprada

                if qtde > qtde_comprada:
                    print(f'A quantidade solicitada é maior que o estoque disponível. O valor foi ajustado para a quantidade máxima de {qtde_comprada}.')

                items_cliente.append([produto[0], produto[1], qtde_comprada, produto[3], valor_total])
        
        continuar = validar_entrada('Deseja continuar adicionando items?(s/n) ')
        if continuar != 's':
            break
    return items_cliente

#TODO formatar a saída
def finalizar_atendimento(clientes):
    print(tabulate(clientes, headers=['Item', 'Produto', 'Qtde', 'Preço', 'Total']))
    

produtos = ler_produtos()
items_cliente = iniciar_atendimento(produtos)
print(items_cliente)


