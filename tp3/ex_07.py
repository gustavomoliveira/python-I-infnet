"""
7 - Verificar Palíndromo

Faça um programa que o usuário entre com uma palavra e verifique se a mesma é palíndromo. 
Uma palavra palíndromo é aquela cuja sequência de letras é simétrica,
permitindo uma leitura idêntica da esquerda para a direita ou da direita para a esquerda.
Exemplo: ovo, osso, reler, anilina. 
"""

def validar_input(msg):
    while True:
        entrada = input(msg).strip().lower()
        if all(char.isalpha() for char in entrada):
            return entrada
        else:
            print('\nERRO: Digite um caractere válido.')

def validar_palindromo():
    palavra = validar_input('\nDigite uma palavra e descubra se ela é um palíndromo: ')
    if palavra[::-1] == palavra:
        return f'\nA palavra {palavra} é palíndromo!\n'
    return f'\nA palavra {palavra} NÃO é um palíndromo...\n'

mensagem = validar_palindromo()
print(mensagem)