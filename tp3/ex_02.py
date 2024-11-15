"""
2 - Validação de Nome e Sobrenome com split

Faça um programa que leia um nome e sobrenome na mesma linha e verifique se a entrada é válida. 
Uma entrada válida é uma regra de negócio, onde o nome e o sobrenome tenham pelo menos dois caracteres. 
Utilize os comandos “split” e “len”. 
Exemplo:  “Lu Ma”. Se a entrada não for válida, exibir uma mensagem de erro e pedir ao usuário uma nova entrada para o nome.
"""

def validar_input(msg):
    while True:
        entrada = input(msg).strip()
        if all(char.isalpha() or char.isspace() for char in entrada):
            return entrada
        else:
            print('ERRO: Digite um caractere válido.')

def validar_nome_sobrenome():
    while True:
        nome_sobrenome = validar_input('Digite o nome e sobrenome(pelo menos 2 caracteres cada): ').split()
        for palavra in nome_sobrenome:
            if len(palavra) >= 2:
                return nome_sobrenome
        else:
            print(f'\nERRO: {" ".join(nome_sobrenome).title()} não cumprem os requisitos indicados.\n')

nome_sobrenome = validar_nome_sobrenome()
print(f'\nOlá, {" ".join(nome_sobrenome).title()}!') 
    