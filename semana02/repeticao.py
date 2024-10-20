""" Loops """

# 1 2 3 4 5 0 while
def entrar_numero():
    num = int(input('Insira um número: '))
    return num

def calcular_media(soma, cont):
    media = soma / cont
    print(f'média = {media}')

FIM = 0
num = entrar_numero()
soma = cont = 0 # ambas as variáveis recebem 0. se usasse ',' não funcionaria já que é somente para unpacking
while(num != FIM):
    soma += num
    cont += 1
    num = entrar_numero()
if cont != 0:
    print(f'soma = {soma}')
    calcular_media(soma, cont)
else:
    print('Não há dados.')

# for
for i in range(10): # decrescente
    print(i, end=' ')
print() # para pular linha

# mesmo código acima usando while
i = 0
while(i < 10):
    print(i, end=' ')
    i += 1 # python não possui incrementação com i++