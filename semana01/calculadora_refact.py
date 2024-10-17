""" Refatoração do código da calculadora """

def menu():
    operacao = input('Qual operação deseja executar?(+, -, *, /) ')
    return operacao

def numero_1():
    num_1 = int(input('Entre com o primeiro valor: '))
    return num_1

def numero_2():
    num_2 = int(input('Entre com o segundo valor: '))
    return num_2

def somar(num_1, num_2):
    resultado = num_1 + num_2
    print(f'A soma entre {num_1} e {num_2} é {resultado}')

def subtrair(num_1, num_2):
    resultado = num_1 - num_2
    print(f'A subtração entre {num_1} e {num_2} é {resultado}')

def multiplicar(num_1, num_2):
    resultado = num_1 * num_2
    print(f'A multiplicação entre {num_1} e {num_2} é {resultado}')

def dividir(num_1, num_2):
    if num_2 == 0:
        print('Erro: divisão por 0.')
    else:
        resultado = num_1 / num_2
        print(f'A divisão entre {num_1} e {num_2} é {resultado}')

def executar_operacao(operacao, num_1, num_2):
    match operacao:
        case '+':
            somar(num_1, num_2)
        case '-':
            subtrair(num_1, num_2)
        case '*':
            multiplicar(num_1, num_2)
        case '/':
            dividir(num_1, num_2)
        case _:
            print('Digite um operador válido.')

operacao = menu()
num_1 = numero_1()
num_2 = numero_2()
executar_operacao(operacao, num_1, num_2)