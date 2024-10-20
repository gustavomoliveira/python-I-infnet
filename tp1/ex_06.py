""" 
6 - Escreva um programa onde o usuário deve adivinhar um número secreto.
O programa deve dizer se o palpite está correto, muito alto ou muito baixo.
 """

def resultado_palpite(palpite, numero):
    while True:
        if numero > palpite:
            print(f'O número é maior!')
            palpite = int(input(f'Tente mais uma vez e lembre-se que o número é MAIOR que o seu último chute ({palpite}): '))
        elif numero < palpite:
            print(f'O número é menor!')
            palpite = int(input(f'Tente mais uma vez e lembre-se que o número é MENOR que o seu último chute ({palpite}): '))
        else:
            print(f'Parabéns! Você adivinhou o número secreto {numero}!')
            break

# importando o módulo random para gerar um número aleatório entre um período determinado
import random

numero = random.randint(1, 10)

palpite = int(input('Chute um número entre 1 e 10: '))

resultado_palpite(palpite, numero)

