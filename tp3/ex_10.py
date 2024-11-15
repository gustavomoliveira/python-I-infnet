"""
10 -  Dia da Semana

Faça um programa que leia um número entre um e sete, e exiba o dia da semana correspondente. 
O programa deverá validar a entrada do usuário. 
Exemplo: Entre com um número: 8

Erro: número inválido

Entre com um número: 1

Domingo

Entre com um número: 7

Sábado
"""

def validar_entrada(msg):
    while True:
        try:
            entrada = int(input(msg))
            if 1 <= entrada <= 7:
                return entrada
            else:
                print('\nERRO: Número inválido.\n')
        except ValueError:
            print('\nERRO: Digite um número inteiro.\n')

def exibir_dia_da_semana(entrada):
    dias = ['Domingo', 'Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira', 'Sábado']
    return dias[entrada - 1]

entrada = validar_entrada('\nDigite um número (1 a 7) para verificar o dia da semana: ')
mensagem = exibir_dia_da_semana(entrada)
print(f'\n{mensagem}\n')