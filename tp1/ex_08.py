""" 
8 - Crie um programa que pergunte a idade do usuário e verifique se ele é maior de idade ou não.
 """

def valida_input(texto):
    while True:
        try:
            numero = int(input(texto))
            return numero
        except ValueError:
            print('Erro: Digite um número válido.')

def verificar_idade(idade):
    if idade >= 18:
        return f'Você tem {idade} anos e é maior de idade.'
    else:
        return f'Você tem {idade} anos e é menor de idade.'

idade = valida_input('Qual a sua idade? ')
resultado = verificar_idade(idade)
print(resultado)