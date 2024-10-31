"""
10 - Números Maiores ou Iguais à Média

Faça um programa que leia uma sequência de números,
terminada pelo número zero, e armazene-os em uma lista.

O programa deve mostrar apenas os números maiores ou iguais à média dos elementos lidos.
Implemente uma função para ler a lista e outra para exibir os números filtrados.
Utilize apenas os comandos ensinados em aula.
"""

def ler_sequencia():
    sequencia = []
    while True:
        try:
            numero = int(input('Digite um número inteiro (ou 0 para encerrar): '))
            if numero == 0:
                break
            else:
                sequencia.append(numero)
        except ValueError:
            print('ERRO: Digite um número válido.')
    return sequencia

def calcular_media(sequencia):
    media = sum(sequencia) / len(sequencia)
    return media

def exibir_filtrados(media, sequencia):
    filtrados = []
    for num in sequencia:
        if num >= media:
            filtrados.append(num)
    return filtrados
    
sequencia = ler_sequencia()
media = calcular_media(sequencia)
filtrados = exibir_filtrados(media, sequencia)
print(f'Os números filtrados - maiores ou iguais a média - são: {filtrados}')