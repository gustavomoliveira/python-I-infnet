"""
1 - Contando Vogais
Faça um programa que leia uma sequência de caracteres terminada por um ponto (.) e mostre o número de vogais digitadas.
Cada caractere deve ser digitado/lido separadamente.

Exemplo:
Entre com um caractere: a
Entre com um caractere: @
Entre com um caractere: x
Entre com um caractere: 2
Entre com um caractere: e
Entre com um caractere: .
Número de vogais: 2
"""

def validar_input(txt):
    while True:
        caractere = input(txt)
        if len(caractere) == 1:
            return caractere
        else:
            print('Digite apenas um caracter.')

def contar_vogais():
    vogais = ('a', 'e', 'i', 'o', 'u')
    total_vogais = 0
    as_vogais = []
    while True:
        caractere = validar_input('Digite um caracter ou "." para encerrar a leitura: ')
        print(f'Caracter digitado: {caractere}')
        if caractere == '.':
            print('Leitura encerrada')
            break
        elif caractere in vogais:
            total_vogais += 1
            as_vogais.append(caractere)
    return total_vogais, as_vogais

total_vogais, as_vogais = contar_vogais()
print(f"""
Vogais digitadas: {', '.join(as_vogais)}.
Número total de vogais digitadas: {total_vogais}.
""")