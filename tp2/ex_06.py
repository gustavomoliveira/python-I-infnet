"""
6 - Números Primos em um Intervalo
Faça um programa que leia um intervalo inferior e
superior e mostre os números primos encontrados nesse intervalo.
Por exemplo, para o intervalo de 5 a 10, a saída será: 5, 7.
O programa também deve mostrar a quantidade de números primos encontrados.
Implemente uma função para verificar se um número é primo.
"""

# números primos: maior do que 1 e / por 1 e ele mesmo

def validar_numeros(txt):
    while True:
        try:
            numero = int(input(txt))
            return numero
        except ValueError:
            print('Digite um número válido.')

def gerar_intervalo(min, max):
    nums_intervalo = []
    for num in range(min, max + 1):
        nums_intervalo.append(num)
    return nums_intervalo

def verificar_primo(num):
    if num < 2:
        return False
    for div in range(2, num):
        if num % div == 0:
            return False
    return True

num_min = validar_numeros('Digite um número para representar um intervalo inferior: ')
num_max = validar_numeros('Digite um número para representar um intervalo superior: ')
nums_intervalo = gerar_intervalo(num_min, num_max)
nums_primos = []

# passa um número por vez do intervalo digitado e, caso primo, é adicionado a lista de números primos.
for num in nums_intervalo:
    if verificar_primo(num):
        nums_primos.append(num)

print(f""" 
---------------VERIFICAÇÃO-----------------

Números primos encontrados: {nums_primos}.
Um total de: {len(nums_primos)} números.

-------------------------------------------
""")