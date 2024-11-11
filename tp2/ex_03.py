
def validar_numeros(txt):
    numeros = []
    while True:
        try:
            numero = int(input(txt))
            if numero == 0:
                print('Calculando fatoriais...')
                print()
                return numeros
            elif numero > 0:
                numeros.append(numero)
            else:
                print('Digite um número inteiro positivo.')
        except ValueError:
            print('ERRO: Digite um número válido.')

def calcular_fatorial(numero):
    resultado = 1
    for num in range(1, numero + 1):
        resultado *= num
    return resultado

def exibir_fatorial(numeros):
    for numero in numeros:
        resultado = calcular_fatorial(numero)
        print(f'O fatorial de {numero} é {resultado}')

numeros = validar_numeros('Digite um número inteiro positivo ou 0 para encerrar: ')
exibir_fatorial(numeros)