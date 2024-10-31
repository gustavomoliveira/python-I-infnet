"""
3- Fatorial de Números Positivos
Faça um programa que leia uma sequência de números inteiros positivos,
terminada por zero. Para cada número lido, mostre seu fatorial.
Implemente uma função para o cálculo do fatorial.
"""

def validar_numeros(txt):
    numeros = []
    while True:
        try:
            numero = int(input(txt))
            if numero == 0:
                print('Calculando fatoriais...')
                return numeros
            elif numero > 0:
                numeros.append(numero)
            else:
                print('Digite um número inteiro positivo.')
        except ValueError:
            print('ERRO: Digite um número válido.')

def calcular_fatorial(numero):
    resultado = 1
    for num in range(1, numero + 1): # +1 para incluir o número
        resultado *= num
    return resultado

numeros = validar_numeros('Digite um número: ')
for numero in numeros:
    resultado = calcular_fatorial(numero)
    print(f'O fatorial de {numero} é {resultado}')