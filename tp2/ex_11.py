
def pedir_numero(txt):
    while True:
        try:
            numero = int(input(txt))
            return numero
            
        except ValueError:
            print('ERRO: Digite um número válido.')

def buscar_elemento(lista, numero):
    if numero in lista:
        return lista.index(numero)
    else:
        return -1
    
def verificar_numero(posicao, numero):
    if posicao != -1:
        print(f"""
-----------------------------------------------------------------
      
O número digitado {numero} se encontra na lista, no índice {posicao}.

Sua posição como elemento nessa lista é a de número {posicao + 1}.

-----------------------------------------------------------------
""")
    else:
        print(f'\nO número {numero} não se encontra na lista. ({posicao})\n')

lista = [20, 10, 30, 40, 60, 50, 70, 90, 80, 100]
numero = pedir_numero('Digite um número: ')
posicao = buscar_elemento(lista, numero)
verificar_numero(posicao, numero)
