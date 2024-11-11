
def par_ou_impar(lista):
    pares = []
    impares = []
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    return pares, impares

lista = [10, 2, 30, 4, 50, 6, 70, 8, 9, 1]
pares, impares = par_ou_impar(lista)
print(f"""
------- Resultado -------
      
Números Pares --> {pares}
Números Ímpares --> {impares}

-------------------------
""")