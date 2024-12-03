import pathlib
from tabulate import tabulate
from crud import *

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
    print(f'\nCaixa aberto. Lista de produtos disponíveis:\n')
    print(tabulate(produtos, headers=['Id', 'Nome', 'Qtde', 'Preço']))
    print('--------------------------------\n')
    return produtos

produtos = ler_produtos()
realizar_atendimento(produtos)


