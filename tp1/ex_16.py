"""
16 - Neste exercício, você deverá escrever um programa em Python que verifique se um número
fornecido pelo usuário é par ou ímpar. Imprima uma mensagem indicando se o número é par ou ímpar.
"""

def valida_input(texto):
    while True:
        try:
            numero = int(input(texto))
            return numero
        except ValueError:
            print('Erro: Digite um número válido.')

def par_ou_impar(numero):
    if numero % 2 == 0:
        return f'O {numero} é par!'
    else:
        return f'O {numero} é ímpar!'

numero = valida_input('Digite um número: ')
resultado = par_ou_impar(numero)
print(resultado)