"""
11 - Formatar CPF

Faça um programa que o usuário entre com um número de CPF
e mostre o número no formato 999.999.999-99.
Exemplo: o usuário entra com o CPF 01234567890 e o programa exibe como saída 012.345.678-90.
A entrada deve ser validada até que o usuário entre com 11 números. Caso contrário, exibir uma mensagem de erro.
"""

def validar_cpf(msg):
    while True:
        entrada = input(msg).strip()
        if all(num.isdigit() for num in entrada) and len(entrada) == 11:
            return f'\n{entrada[:3]}.{entrada[3:6]}.{entrada[6:9]}-{entrada[9:]}\n'
        else:
            print(f'\nERRO: O número do CPF precisa de 11 dígitos e apenas números.\n')

mensagem = validar_cpf('\nDigite um número de CPF com 11 dígitos e apenas dígitos: ')
print(mensagem)