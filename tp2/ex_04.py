
def calcular_tabuada(numero):
    resultado = 0
    for mult in range(1, 11):
        resultado = numero * mult
        print(f'{numero} x {mult} = {resultado}')

def exibir_tabuada(numeros):
    for numero in numeros:
        print(f'A tabuada de {numero}:')
        calcular_tabuada(numero)
        print()
    
numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
exibir_tabuada(numeros)