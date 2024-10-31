"""
5 - Progressão Aritmética
Uma progressão aritmética (PA) é uma sequência numérica onde cada termo,
a partir do segundo, é igual à soma do termo anterior com uma constante.
A constante é a diferença entre o segundo e o primeiro número.
Faça um programa que receba dois números inteiros e, a partir dessa informação, gere uma sequência em PA.
"""

def validar_input(txt):
    while True:
        try:
            numero = int(input(txt))
            return numero
        except ValueError:
            print('Digite um número válido.')

def calcular_pa(num1, num2, size):
    pa = []
    const = num2 - num1
    for n in range(1, size + 1):
        prox_num = num1 + (n - 1) * const
        pa.append(prox_num)
    return pa

num1 = validar_input('Digite o primeiro número: ')
num2 = validar_input('Digite o segundo número: ')
size = validar_input('Digite o tamanho total que a PA deve ter: ')
pa = calcular_pa(num1, num2, size)
print(f'Progressão Aritmética: {pa}')
