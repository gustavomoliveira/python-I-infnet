
def validar_sequencia(txt):
    sequencia = []
    while True:
        try:
            numero = int(input(txt))
            if numero == 0:
                print('\nA sequência de números inseridos está encerrada.')
                break
            else:
                sequencia.append(numero)
        except ValueError:
            print('\nERRO: Digite um número válido.\n')
    return sequencia
                
def ler_numeros(sequencia):
    for numero in sequencia:
        print(numero, end=" ")

def exibir_lista_invertida(sequencia):
    print(f'\n\nSequência de números invertida: {sequencia[::-1]}\n')
    
sequencia = validar_sequencia('Digite um número ou 0 para encerrar: ')
ler_numeros(sequencia)
exibir_lista_invertida(sequencia)