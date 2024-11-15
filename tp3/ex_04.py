"""
4 -  Data em Formato Inteiro

Faça um programa que leia uma data no formato “dd/mm/aaaa” e mostre o dia, mês e ano no formato de inteiros.
"""
from datetime import datetime

def validar_entrada(msg):
    while True:
        try:
            entrada = input(msg)
            if datetime.strptime(entrada, "%d/%m/%Y"):
                return str(entrada)
        except ValueError:
            print('\nERRO: Digite uma data existente e no formato dd/mm/aaaa.')

def data_formato_inteiro():
    entrada = validar_entrada('\nDigite uma data no formato dd/mm/aaaa: ').split('/')
    dia = int(entrada[0])
    mes = int(entrada[1])
    ano = int(entrada[2])
    return dia, mes, ano

def validar_inteiros(dia, mes, ano):
    if all(isinstance(valor, int) for valor in [dia, mes, ano]):
        print(f'\nA data {dia:02d}/{mes:02d}/{ano} é composta por números inteiros.\n')
    else:
        print(f'\nA data {dia:02d}/{mes:02d}/{ano} NÃO é composta por números inteiros.\n')

dia, mes, ano = data_formato_inteiro()
validar_inteiros(dia, mes, ano)

