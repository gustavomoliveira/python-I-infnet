"""
Leia uma sequência de números terminada por zero e mostre
os números maiores ou iguais a média
"""

# iniciando mockando os dados. dados fake.

def entrar_numeros():
    FIM = 0
    numeros = []
    num = int(input('Entre com o número: '))
    while num != FIM:
        numeros.append(num)
        num = int(input('Entre com o número: '))
    return numeros

def exibir_numeros(numeros):
    for num in numeros:
        print(num, end=' ')
    print()

def calcular_media(numeros):
    soma = 0
    for num in numeros:
        soma += num
    media = soma / len(numeros)   
    return media

def exibir_numeros_maiores_iguais_media(numeros, media):
    print('Números maiores ou iguais a média.')
    for num in numeros:
        if num >= media:
            print(num, end=' ')

numeros = entrar_numeros()
exibir_numeros(numeros)
media = calcular_media(numeros)
print(f'Média = {media}')
exibir_numeros_maiores_iguais_media(numeros, media)