"""
9 - Números em Ordem Invertida

Faça um programa que leia uma sequência de números,
terminada pelo número zero, e mostre-os na ordem invertida.

Implemente uma função para ler a lista de números e outra para exibir a lista invertida.
Utilize apenas os comandos ensinados em aula.
"""

def validar_sequencia(txt):
    sequencia = []
    while True:
        try:
            numero = int(input(txt))
            if numero == 0:
                print('A sequência de números inseridos está encerrada.')
                break
            else:
                sequencia.append(numero)
        except ValueError:
            print('ERRO: Digite um número válido.')
    return sequencia
                
def ler_numeros(sequencia):
    for numero in sequencia:
        print(numero, end=" ")

def exibir_lista_invertida(sequencia):
    print(f'Sequência de números invertida: {sequencia[::-1]}')
    

sequencia = validar_sequencia('Digite um número: ')
ler_numeros(sequencia)
exibir_lista_invertida(sequencia)