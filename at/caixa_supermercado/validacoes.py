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
        if entrada in ('s', 'n'):
            return entrada
        else:
            print('ERRO: Digite "s" para sim e "n" para não.')