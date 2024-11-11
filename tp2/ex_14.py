
def validar_entrada():
    while True:
        try:
            numero = int(input('Digite um número maior ou igual a zero: '))
            if numero >= 0:
                return numero
            else:
                print('ERRO: Digite um número maior ou igual a zero!')
        except ValueError:
            print('ERRO: Digite apenas números válidos.')

numero = validar_entrada()
print(f"""
Número digitado --> {numero}.
""")