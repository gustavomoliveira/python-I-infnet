""" 
2 - Faça um programa que converta um número fornecido de minutos em horas e minutos,
e depois faça o inverso, convertendo horas e minutos de volta para minutos totais.
"""

def valida_input(texto):
    while True:
        try:
            numero = int(input(texto))
            return numero
        except ValueError:
            print('Erro: digite um número válido.')

def converte_em_horas(num):
    horas =  num // 60
    minutos = num % 60
    f'{horas}:{minutos:02d}hrs.'
    return horas, minutos, f'{horas}:{minutos:02d}hrs.'

def converte_em_minutos(horas, minutos):
    minutos_totais = (horas * 60) + minutos
    return minutos_totais

numero_fornecido = valida_input('Digite um número inteiro: ')

horas, minutos, mensagem = converte_em_horas(numero_fornecido)
print(mensagem)

minutos_totais = converte_em_minutos(horas, minutos)
print(f'{minutos_totais} minutos.')
