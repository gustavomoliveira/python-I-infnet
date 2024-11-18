"""
16 - Cálculo de Média com f-strings

Faça um programa que leia dois números e mostre a média dos números lidos.
Utilize a formatação “f-strings” para a exibição da saída.
"""

def validar_num(msg):
    while True:
        try:
            num = int(input(msg))
            return num
        except ValueError:
            print('ERRO: Digite um número.')

def calcular_media(num1, num2):
    media = (num1 + num2) / 2
    return media

num1 = validar_num('\nDigite o primeiro número: ')
num2 = validar_num('\nDigite o segundo número: ')
media = calcular_media(num1, num2)
print(f'\nA média entre {num1} e {num2} é igual a {media}.\n')
