import pathlib
from models import Conta

DIR_CUR = pathlib.Path(__file__).parent.resolve() # gera automaticamente o caminho do arquivo e o torna flexível

ARQ = str(DIR_CUR) + '/contas.csv'

""" def ler_contas():
    contas = []
    try:
        with(open(ARQ, 'r', encoding='UTF-8') as arquivo):
            linha = arquivo.readline()
            while linha != '':
                linha = linha.strip('\n') --> existe um \n ao final de cada linha do arquivo csv
                campos = linha.split(',')
                id = int(campos[0])
                nome = campos[1]
                saldo = float(campos[2])
                conta = Conta(id, nome, saldo)
                contas.append(conta)
                linha = arquivo.readline()
    except:
        print('ERRO: Leitura do arquivo.')
    return contas
 """

# mesma função em pythonic
def ler_contas():
    contas = []
    try:
        with(open(ARQ, 'r', encoding='UTF-8') as arquivo):
            while linha := arquivo.readline():
                campos = linha.strip('\n').split(',')
                id, nome, saldo = int(campos[0]), campos[1], float(campos[2])
                contas.append(Conta(id, nome, saldo))
    except:
        print('ERRO: Leitura do arquivo.')
    return contas

def gravar_contas(contas):
    try:
        with(open(ARQ, 'w', encoding='UTF=8') as arquivo):
            for conta in contas:
                arquivo.write(f'{conta.id},{conta.nome},{conta.saldo}\n')
    except:
        print('ERRO: Gravação impossível.')