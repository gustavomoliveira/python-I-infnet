from crud import *
from arquivo import *

def realizar_atendimento(produtos):
    clientes = []
    proximo_cliente_id = 1
    exibir_estoque(produtos)
    while True:
        opcao = menu()
        match opcao:
            case 1:
                cliente, proximo_cliente_id = iniciar_atendimento(produtos, proximo_cliente_id)
                clientes.append(cliente)
            case 2:
                conferir_estoque(produtos)
            case 0:
                fechar_caixa(clientes, produtos)
                break
            case _:
                print('ERRO: Opção inválida.')
    #gravar_produtos(produtos)

produtos = ler_produtos()
realizar_atendimento(produtos)


