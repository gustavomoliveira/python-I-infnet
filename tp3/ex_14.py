"""
14 - Cinco Primeiros e Últimos Caracteres

Faça um programa que leia a frase abaixo e mostre os cinco primeiros e os
cinco últimos caracteres, utilizando o comando [::] de manipulação de strings. 
Exemplo: Entre com uma frase: eu gosto de programar

Cinco primeiros: eu go

Cinco últimos: ramar
"""

def validar_frase(msg):
    while True:
        frase = input(msg).strip()
        if all(char.isalpha() or char.isspace() for char in frase):
            return frase
        else:
            print('\nERRO: Digite apenas letras.\n')

def fatiar_frase():
    frase = validar_frase('\nDigite uma frase qualquer: ')
    cinco_primeiros = frase[:5]
    cinco_ultimos = frase[-5:]
    return cinco_primeiros, cinco_ultimos

cinco_primeiros, cinco_ultimos = fatiar_frase()
print(f'\nCinco primeiros caracteres: {cinco_primeiros}')
print(f'\nCinco últimos caracteres: {cinco_ultimos}\n')
