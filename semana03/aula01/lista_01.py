""" Listas """

# não é vetor nem array

lista = [13, 3.14, True, 'Gustavo'] # lista em Py, assim como em JS, aceita vários tipos em uma mesma lista

lista.append('Bartolomeu') # append insere ao final da lista
lista.insert(1, 'Cachorro') # insert pode ser determinada a posição

print(lista)
print(len(lista))
print(lista[0])
print(lista[1], lista[2], lista[3])
print(lista.pop(0)) # remove o ultimo ou passando o índice
print(lista.remove('Cachorro')) # remove pelo elemento

# iterando sob a lista, através do índice
for i in range(len(lista)):
    print(lista[i], end=' ') # pythonic com end para tudo ficar na mesma linha
print()

# simulando um forEach() de JS, iterando sob elementos da lista
for el in lista:
    print(el, end=' ')