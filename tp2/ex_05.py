
def validar_input(txt):
    while True:
        try:
            numero = int(input(txt))
            return numero
        except ValueError:
            print('Digite um número válido.')

def calcular_pa(num1, num2, tamanho):
    pa = []
    const = num2 - num1
    for n in range(1, tamanho + 1):
        prox_num = num1 + (n - 1) * const
        pa.append(prox_num)
    return pa

num1 = validar_input('Digite o primeiro número: ')
num2 = validar_input('Digite o segundo número: ')
tamanho = validar_input('Digite o tamanho total que a PA deve ter: ')
pa = calcular_pa(num1, num2, tamanho)
print(f'Progressão Aritmética: {pa}')
