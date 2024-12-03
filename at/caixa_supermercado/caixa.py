from tabulate import tabulate
from crud import *
from arquivo import *

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

produtos = ler_produtos()
realizar_atendimento(produtos)


