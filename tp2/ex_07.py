"""
7 - Exibir Lista Invertida
Faça um programa que defina a lista:
[10, 20, 30, 40, 50, 60, 70, 80]
e mostre seu conteúdo na ordem invertida.
Utilize apenas os comandos ensinados em aula.
"""

def inverter_lista(lista):
    lista_invertida = lista[::-1]
    return lista_invertida

lista = [10, 20, 30, 40, 50, 60, 70, 80]
lista_invertida = inverter_lista(lista)
print(f'Lista invertida --> {lista_invertida}')

