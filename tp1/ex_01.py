"""
1 - Crie um programa que peça ao usuário para inserir dois números e,
em seguida, calcule e exiba a soma, subtração, multiplicação, divisão e divisão inteira desses números.
"""

def soma(num_1, num_2):
    resultado = num_1 + num_2
    print(f'Resultado da soma é {resultado}')

def subtracao(num_1, num_2):
    resultado = num_1 - num_2
    print(f'Resultado da subtração é {resultado}')

def multiplicacao(num_1, num_2):
    resultado = num_1 * num_2
    print(f'Resultado da multiplicação é {resultado}')

def divisao(num_1, num_2):
    if num_2 != 0:
        resultado = num_1 / num_2
        print(f'Resultado da divisão é {resultado:.2f}')
    else:
        print('Erro: divisão por 0.')

def divisao_inteira(num_1, num_2):
    if num_2 != 0:
        resultado = num_1 // num_2
        print(f'Resultado da divisão inteira é {resultado}')
    else:
        print('Erro: divisão por 0.')

num_1 = float(input('Digite o primeiro número: '))
num_2 = float(input('Digite o segundo número: '))

soma(num_1, num_2)
subtracao(num_1, num_2)
multiplicacao(num_1, num_2)
divisao(num_1, num_2)
divisao_inteira(num_1, num_2)