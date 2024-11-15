"""
12 - TInverter Frase com for

Faça um programa que leia a frase abaixo e mostre a frase invertida,
utilizando o comando de repetição “for”. 
Exemplo: Entre com uma frase: eu gosto de programar 

ramargorp ed otsog ue
"""

def validar_frase(msg):
    while True:
        frase = input(msg).strip()
        if all(char.isalpha() or char.isspace() for char in frase):
            return frase
        else:
            print('\nERRO: Digite apenas letras.\n')

def inverter_frase():
    frase = validar_frase('\nDigite uma frase: ')
    frase_invertida = ''

    for char in reversed(frase):
        frase_invertida += char
    return frase_invertida

frase_invertida = inverter_frase()
print(f'\n{frase_invertida}\n')
