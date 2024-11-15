"""
5 - Validação de Data

Refaça o programa anterior de forma validar a data,
verificando os meses com 31, 30, 29, e 28 dias, além do mês ser válido. 
Exemplo: Para a entrada “29/02/2024”, o programa deverá exibir “data válida”.
Para a entrada “29/02/2023”, o programa deverá exibir “data inválida”.
"""

def converter_data():
    entrada = input('\nDigite uma data no formato dd/mm/aaaa: ').split('/')
    dia = int(entrada[0])
    mes = int(entrada[1])
    ano = int(entrada[2])
    return dia, mes, ano

def fevereiro_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def validar_mes(mes):
    if mes < 1 or mes > 12:
        print(f'ERRO: Mês inválido')
        return False
    return True

def validar_dias(dia, mes, ano):
    dias_nos_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if mes == 2 and fevereiro_bissexto(ano):
        dias_nos_meses[1] = 29

    if dia < 1 or dia > dias_nos_meses[mes - 1]:
        return False
    return True
        
def validar_data(dia, mes, ano):
    if not validar_mes(mes) or not validar_dias(dia, mes, ano):
        return f'\nA data {dia:02d}/{mes:02d}/{ano} NÃO é válida.\n'
    return f'\nA data {dia:02d}/{mes:02d}/{ano} é válida.\n'
              
dia, mes, ano = converter_data()
mensagem = validar_data(dia, mes, ano)
print(mensagem)
