""" 
8 - Crie um programa que pergunte a idade do usuário e verifique se ele é maior de idade ou não.
 """

def verificar_idade(idade):
    if idade >= 18:
        print(f'Você tem {idade} anos e é maior de idade.')
    else:
        print(f'Você tem {idade} anos e é menor de idade.')

idade = int(input('Qual a sua idade? '))
verificar_idade(idade)