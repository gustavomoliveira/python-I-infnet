def validar_id(msg, produtos):
    while True:
        try:
            id = int(input(msg))
            if 1 <= id <= len(produtos):
                return id
            else:
                print(f'\nERRO: Produto não cadastrado. Escolha um id de 1 a {len(produtos)}.\n')
        except ValueError:
            print('\nERRO: Digite um número inteiro para o id.\n')

def validar_qtde(msg):
    while True:
        try:
            qtde = int(input(msg))
            if qtde > 0:
                return qtde
            else:
                print('\nERRO: A quantidade inserida deve ser maior que 0.\n')
        except ValueError:
            print('\nERRO: Digite um número inteiro para a quantidade.\n')

def validar_opcao(msg):
    while True:
        try:
            opcao = int(input(msg))
            if 0 <= opcao <= 2:
                return opcao
            else:
                print('\nERRO: Opção inválida. Escolha uma das opções de atendimento.\n')
        except ValueError:
            print('\nERRO: Digite entre 0 a 2 para selecionar uma opção.\n')

def validar_entrada(msg):
    while True:
        entrada = input(msg).strip().lower()
        if entrada in ('s', 'n'):
            return entrada
        else:
            print('\nERRO: Digite "s" para sim e "n" para não.\n')