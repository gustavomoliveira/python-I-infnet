"""
3 - Exibir Sobrenome, Nome

Faça um programa que leia um nome e sobrenome na mesma linha. 
O programa deverá exibir o nome no formato “SOBRENOME, Nome”. 
Exemplo: O nome “Maria Maia”, deverá ser apresentado como “MAIA, Maria”.
"""
def validar_input(msg):
    while True:
        entrada = input(msg).strip()
        if all(char.isalpha() or char.isspace() for char in entrada):
            return entrada
        else:
            print('\nERRO: Digite caracteres válidos.\n')

def exibir_sobrenome_nome():
    while True:
        entrada = validar_input('Digite seu nome e sobrenome: ').split()
        if len(entrada) < 2:
            print('\nERRO: Digite, pelo menos, um nome e um sobrenome.\n')
        else:
            nome = ' '.join(entrada[:-1]).title()
            sobrenome = ' '.join(entrada[-1:]).upper()
            return sobrenome, nome
    
sobrenome, nome = exibir_sobrenome_nome()
print(f'\n{sobrenome}, {nome}\n')