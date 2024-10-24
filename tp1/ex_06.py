""" 
6 - Escreva um programa onde o usuário deve adivinhar um número secreto.
O programa deve dizer se o palpite está correto, muito alto ou muito baixo.
 """

def valida_input(texto):
    while True:
        try:
            numero = int(input(texto))
            if 1 <= numero <= 50:
                return numero
            else:
                print('Erro: Digite um número entre 1 e 50.')
        except ValueError:
            print('Erro: Digite um número válido.')

def resultado_palpite(numero):
    palpite = valida_input('Chute um número entre 1 e 50: ')
    while palpite != numero:
        if palpite < numero:
            print(f'O número é maior!')
            palpite = valida_input(f'Tente mais uma vez e lembre-se que o número é MAIOR que o seu último chute ({palpite}): ')
        else:
            print(f'O número é menor!')
            palpite = valida_input(f'Tente mais uma vez e lembre-se que o número é MENOR que o seu último chute ({palpite}): ')
    
    print(f'Parabéns! Você adivinhou o número secreto {numero}!')

# importando o módulo random para gerar um número aleatório entre um período determinado
import random

# como exemplo do exercício, ajustei o range numérico dessa forma
numero = random.randint(1, 50)

resultado_palpite(numero)

