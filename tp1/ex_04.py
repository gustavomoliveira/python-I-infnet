""" 
4 - Desenvolva um programa que peça ao usuário para escolher uma operação(adição, subtração, multiplicação, divisão)
e dois números, e então execute a operação escolhida com os números.
 """

def selecao_operacao_e_numeros():
    operacao = int(input('Escolha a operação que será realizada: '))
    if operacao < 0 or operacao > 4:
        print('Opção incorreta. Escolha uma opção válida no Menu.')
        return operacao, None, None
    else:
        num_1 = int(input('Digite o primeiro número: '))
        num_2 = int(input('Digite o segundo número: '))
        return operacao, num_1, num_2
    
def adicao(num_1, num_2):
    result = num_1 + num_2
    print(f'O resultado da adição é {result}')

def subtracao(num_1, num_2):
    result = num_1 - num_2
    print(f'O resultado da subtração é {result}')

def multiplicacao(num_1, num_2):
    result = num_1 * num_2
    print(f'O resultado da multiplicação é {result}')

def divisao(num_1, num_2):
    if num_2 != 0:
        result = num_1 / num_2
        print(f'O resultado da divisão é {result}')
    else:
        print('Erro: divisão por 0.')

def executar_operacao(operacao, num_1, num_2):
    if num_1 is None or num_2 is None:
        return
    match operacao:
        case 1:
            adicao(num_1, num_2)
        case 2:
            subtracao(num_1, num_2)
        case 3:
            multiplicacao(num_1, num_2)
        case 4:
            divisao(num_1, num_2)
        case _:
            print('Retornando ao Menu de seleção.')

menu = """ 
------- MENU -------
[1] - Adição
[2] - Subtração
[3] - Multiplicação
[4] - Divisão
--------------------
 """

print(menu)
operacao, num_1, num_2 = selecao_operacao_e_numeros()

if num_1 is not None or num_2 is not None:
    executar_operacao(operacao, num_1, num_2)
