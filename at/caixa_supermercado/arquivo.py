import pathlib

DIR_CUR = pathlib.Path(__file__).parent.resolve()
ARQ = str(DIR_CUR) + '/produtos.csv'

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
    return produtos

def gravar_produtos(produtos):
    try:
        with(open(ARQ, 'w', encoding='UTF=8') as arquivo):
            for produto in produtos:
                arquivo.write(f'{produto[0]},{produto[1]},{produto[2]},{produto[3]}\n')
    except:
        print('ERRO: Gravação impossível.')