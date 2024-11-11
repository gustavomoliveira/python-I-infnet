
def menor_numero(lista):
    menor = min(lista)
    return menor

def maior_numero(lista):
    maior = max(lista)
    return maior

def soma_numeros(lista):
    soma = sum(lista)
    return soma

def media_numeros(lista):
    media = sum(lista) / len(lista)
    return media

lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
menor = menor_numero(lista)
maior = maior_numero(lista)
soma = soma_numeros(lista)
media = media_numeros(lista)

print(f"""
----- RESULTADOS -----
      
Menor número --> {menor}
Maior número --> {maior}
A soma dos números --> {soma}
A média dos números --> {media}

-----------------------
""")