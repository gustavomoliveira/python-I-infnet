""" Calculadora com Match Case"""

num_1 = int(input('Entre com o primeiro valor: '))
num_2 = int(input('Entre com o segundo valor: '))
operacao = input('Qual operação deseja executar?(+, -, *, /) ')

match operacao:
    case '+':
        print(f'A soma entre {num_1} e {num_2} é {num_1 + num_2}')
    case '-':
        print(f'A subtração entre {num_1} e {num_2} é {num_1 - num_2}')
    case '*':
        print(f'A multiplicação entre {num_1} e {num_2} é {num_1 * num_2}')
    case '/':
        if num_2 == 0:
            print('Divisão por 0.')
        else:
            print(f'A divisão entre {num_1} e {num_2} é {num_1 / num_2}')
    case _:
        print('Digite um operador válido.') # em python se trata o default com '_'


