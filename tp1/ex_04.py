""" 
4 - Desenvolva um programa que peça ao usuário para escolher uma operação(adição, subtração, multiplicação, divisão)
e dois números, e então execute a operação escolhida com os números.
 """

# Função de validação de inputs int()
def valida_inputs(texto):
    while True:
        try:
            numero = int(input(texto))
            return numero
        except ValueError:
            print('Erro: Digite um número válido.')

# Função que valida a escolha da operação
def valida_selecao_operacao():
    while True:
        operacao = valida_inputs('Escolha a operação que será realizada: ')
        if operacao < 1 or operacao > 4:
            print('Opção incorreta. Escolha uma opção válida no Menu.')
        else:
            return operacao
    
# Adição
def adicao(num_1, num_2):
    result = num_1 + num_2
    print(f'O resultado da adição é {result}')

# Subtração
def subtracao(num_1, num_2):
    result = num_1 - num_2
    print(f'O resultado da subtração é {result}')

 # Multiplicação   
def multiplicacao(num_1, num_2):
    result = num_1 * num_2
    print(f'O resultado da multiplicação é {result}')

# Divisão
def divisao(num_1, num_2):
    if num_2 != 0:
        result = num_1 / num_2
        print(f'O resultado da divisão é {result}')
    else:
        print('Erro: divisão por 0.')

# Função que executa a operação escolhida
def executar_operacao(operacao, num_1, num_2):
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
operacao = valida_selecao_operacao()
num_1 = valida_inputs('Digite o primeiro número: ')
num_2 = valida_inputs('Digite o segundo número: ')

executar_operacao(operacao, num_1, num_2)
