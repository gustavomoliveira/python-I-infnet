""" 
11 - Faça um programa que simule o lançamento de um dado.
O usuário deve escolher quantos dados jogar e o programa deve exibir os resultados.
 """

def valida_input(texto):
    while True:
        try:
            numero = int(input(texto))
            return numero
        except ValueError:
            print('Erro: Digite um número válido.')

def valida_tipo_dado():
    tipo_dados = valida_input('Qual tipo de dado você deseja usar (1 - 6)? ')
    quantidade_dados = valida_input('Quantos dados você deseja jogar? ')    
    if tipo_dados == 1:
        tipo_dados = 4
    elif tipo_dados == 2:
        tipo_dados = 6
    elif tipo_dados == 3:
        tipo_dados = 8
    elif tipo_dados == 4:
        tipo_dados = 10
    elif tipo_dados == 5:
        tipo_dados = 12
    else:
        tipo_dados = 20
    return tipo_dados, quantidade_dados

def rolagem_dados(tipo, qtde):
    numero_dados = 0
    for dado in range(qtde):
        dado = random.randint(1, tipo)
        numero_dados += 1
        print(f'Dado {numero_dados}: {dado}')

import random

os_dados = """ 
-------- DADOS ---------
[1] - Dado de 4 lados (D4)
[2] - Dado de 6 lados (D6)
[3] - Dado de 8 lados (D8)
[4] - Dado de 10 lados (D10)
[5] - Dado de 12 lados (D12)
[6] - Dado de 4 lados (D20)
------------------------
"""

print(os_dados)
tipo_dados, quantidade_dados = valida_tipo_dado()
rolagem_dados(tipo_dados, quantidade_dados)
