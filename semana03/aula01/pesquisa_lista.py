lista = [5, 4, 1, 2, 7, 9, 3, 6, 8, 10]
print(lista)

def pesquisar(num, lista):
    achou = False
    for i in range(len(lista)):
        if(lista[i] == num):
            achou = True
            break
    return achou

def pesquisar2(num, lista):
    achou = False
    for el in lista:
        if(el == num):
            achou = True
            break
    return achou

num = 16
achou = pesquisar2(num, lista)
print(achou)

# terceira forma
print(num in lista)