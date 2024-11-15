"""
8 -  Contagem de Vogais

Faça um programa que o usuário entre com uma
frase e exiba o número de vogais contida na frase. 
Exemplo: “Ana Paula” tem cinco vogais.
"""

def validar_input(msg):
    while True:
        entrada = input(msg).strip()
        if all(char.isalpha() or char.isspace() for char in entrada):
            return entrada
        else:
            print('ERRO: Digite apenas letras e espaços.')

def contar_vogais():
    entrada = validar_input('\nDigite uma palavra ou frase para contar suas vogais: ')
    vogais = ['a', 'e', 'i', 'o', 'u']
    contador = 0
    
    for letra in entrada:
        if letra in vogais:
            contador += 1
    return f'\nVocê digitou "{entrada.title()}" que possui {contador} vogais.\n'
    
mensagem = contar_vogais()
print(mensagem)

