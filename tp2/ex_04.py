"""
4 - Tabuada de 1 a 10
Faça um programa que mostre a tabuada dos números de 1 a 10.
"""

def calcular_tabuada(numero):
    resultado = 0
    for mult in range(1, 11):
        resultado = numero * mult
        print(f'{numero} x {mult} = {resultado}')
    
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for numero in numeros:
    print(f'A tabuada de {numero}:')
    calcular_tabuada(numero)
    print()