""" 1 - Concatenar Nome e Sobrenome

Escreva um programa que leia um nome e depois leia um sobrenome. 
O programa deverá exibir o nome e o sobrenome na mesma linha, utilizando o operador de concatenação.
Exemplo: Entre com o nome: Maria

Entre com o sobrenome: Maia

Maria Maia
"""

def validar_nome_sobrenome(msg):
    while True:
        palavra = input(msg).strip()
        if all(char.isalpha() or char.isspace() for char in palavra):
            return palavra
        else:
            print('ERRO: Digite apenas letras/caracteres.')

def nome_e_sobrenome():
    nome = validar_nome_sobrenome('\nDigite o nome: ').title()
    sobrenome = validar_nome_sobrenome('\nDigite o sobrenome: ').title()
    print()
    print(nome + ' ' + sobrenome)

nome_e_sobrenome()