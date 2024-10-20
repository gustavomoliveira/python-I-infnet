""" 
11 - Faça um programa que simule o lançamento de um dado.
O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados.
 """

def rolagem_dados(qtde):
    numero_dado = 0
    for dado in range(qtde):
        dado = random.randint(1, 6)
        numero_dado += 1
        print(f'Dado {numero_dado}: {dado}')

import random
quantidade_dados = int(input('Quantos dados você deseja jogar? '))
rolagem_dados(quantidade_dados)
