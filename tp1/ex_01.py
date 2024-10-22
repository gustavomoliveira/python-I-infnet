"""
1 - Crie um programa que peça ao usuário para inserir dois números e,
em seguida, calcule e exiba a soma, subtração, multiplicação, divisão e divisão inteira desses números.
"""

def soma(num_1, num_2):
    resultado = num_1 + num_2
    return f'Resultado da soma é {resultado}'

def subtracao(num_1, num_2):
    resultado = num_1 - num_2
    return f'Resultado da subtração é {resultado}'

def multiplicacao(num_1, num_2):
    resultado = num_1 * num_2
    return f'Resultado da multiplicação é {resultado}'

def divisao(num_1, num_2):
    if num_2 != 0:
        resultado = num_1 / num_2
        return f'Resultado da divisão é {resultado:.2f}'
    else:
        return 'Erro: divisão por 0.'

def divisao_inteira(num_1, num_2):
    if num_2 != 0:
        resultado = num_1 // num_2
        return f'Resultado da divisão inteira é {resultado}'
    else:
        return 'Erro: divisão por 0.'

num_1 = float(input('Digite o primeiro número: '))
num_2 = float(input('Digite o segundo número: '))

resultado_soma = soma(num_1, num_2)
print(resultado_soma)

resultado_subtracao = subtracao(num_1, num_2)
print(resultado_subtracao)

resultado_multiplicacao = multiplicacao(num_1, num_2)
print(resultado_multiplicacao)

resultado_divisao = divisao(num_1, num_2)
print(resultado_divisao)

resultado_divisao_inteira = divisao_inteira(num_1, num_2)
print(resultado_divisao_inteira)
