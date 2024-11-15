"""
6 - Formato “dia de mês de ano”

Faça um programa que leia uma data no formato “dd/mm/aaaa” e
mostre o dia, mês e ano no formato “dia de nome_do_mês de ano”. 
Exemplo: Para a entrada “02/11/2024” o programa deverá exibir “02 de novembro de 2024”.
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

def converter_data():
    entrada = validar_entrada('\nDigite uma data no formato dd/mm/aaaa: ').split('/')
    dia = int(entrada[0])
    mes = int(entrada[1])
    ano = int(entrada[2])
    return dia, mes, ano

def escrever_data(dia, mes, ano):
    nomes_meses = [
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    ]
    nome_mes = nomes_meses[mes -1]
    return f'\n{dia:02d} de {nome_mes} de {ano}\n.'

dia, mes, ano = converter_data()
mensagem = escrever_data(dia, mes, ano)
print(mensagem)