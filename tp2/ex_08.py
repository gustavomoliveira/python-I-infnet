
def somar_listas(lista1, lista2):
    lista3 = []
    for num1, num2 in zip(lista1, lista2):
        num3 = num1 + num2
        lista3.append(num3)
    return lista3

lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
lista2 = [10, 20, 30, 40, 50, 60, 70, 80]
lista3 = somar_listas(lista1, lista2)
print(f'\nTerceira lista --> {lista3}\n')