"""
9 - Formatar Número de Telefone

Faça um programa que o usuário entre com um número
de telefone e mostre o número no formato (99) 99999-9999.
Exemplo: o usuário entra com o número 21987654321 e o programa
exibe como saída (21) 98765-4321. A entrada deve ser validada
até que o usuário entre com 11 números. Caso contrário, exibir uma mensagem de erro.
"""

def validar_telefone(msg):
    while True:
        entrada = input(msg).strip()
        if all(num.isdigit() for num in entrada) and len(entrada) == 11:
            return f'\n({entrada[:2]}) {entrada[2:7]}-{entrada[7:]}\n'
        else:
            print(f'\nERRO: O número de telefone precisa de 11 dígitos e apenas números.\n')

mensagem = validar_telefone('\nDigite um número de telefone com 11 dígitos: ')
print(mensagem)