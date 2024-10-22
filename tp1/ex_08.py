""" 
8 - Crie um programa que pergunte a idade do usuário e verifique se ele é maior de idade ou não.
 """

def verificar_idade(idade):
    if idade >= 18:
        return f'Você tem {idade} anos e é maior de idade.'
    else:
        return f'Você tem {idade} anos e é menor de idade.'

idade = int(input('Qual a sua idade? '))

resultado = verificar_idade(idade)
print(resultado)