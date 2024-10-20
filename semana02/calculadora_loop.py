""" Calculadora com loop """

def exibir_menu():
    print(""" 
----- MENU ------
[1] - Somar
[2] - Subtrair
[3] - Multiplicar
[4] - Dividir
[0] - Sair
""")

def entrar_operacao():
    while True:
        operacao = int(input('Digite qual operação deseja executar: '))
        if (operacao < 0) or (operacao > 4):
            print('Erro: operação inválida.')
        else:
            break
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
        case 1:
            somar(num_1, num_2)
        case 2:
            subtrair(num_1, num_2)
        case 3:
            multiplicar(num_1, num_2)
        case 4:
            dividir(num_1, num_2)
        case _:
            print('Digite um operador válido.')

exibir_menu()
operacao = entrar_operacao()
while operacao != 0:
    num_1 = numero_1()
    num_2 = numero_2()
    executar_operacao(operacao, num_1, num_2)
    operacao = entrar_operacao()