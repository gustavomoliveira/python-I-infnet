"""
14 - Entrada Validada de Números

Faça um programa que leia um número do teclado e garanta
que ele seja maior ou igual a zero.

Enquanto a entrada não for válida, o programa deve exibir
uma mensagem de erro e pedir uma nova entrada.
Utilize apenas os comandos ensinados em aula.
"""

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