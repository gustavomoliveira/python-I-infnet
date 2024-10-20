""" 
10 - Escreva um programa que combine elementos aleatórios de listas diferentes
(personagens, ações, locais) para criar uma história curiosa.
 """

def combina_listas(personagens, acoes, locais):
    index_personagens = random.randint(0, len(personagens) -1) # garante random index independente do tamanho das listas
    index_acoes = random.randint(0, len(acoes) -1)
    index_locais = random.randint(0, len(locais) -1)
    
    if personagens[index_personagens] == 'peach':
        print(f'A {personagens[index_personagens].capitalize()} {acoes[index_acoes]} no {locais[index_locais]}')
    else:
        print(f'O {personagens[index_personagens].capitalize()} {acoes[index_acoes]} no {locais[index_locais]}')


import random
personagens = ['mario', 'luigi', 'yoshi', 'bowser', 'peach']
acoes = ['pulou', 'correu', 'gritou', 'caiu', 'chorou']
locais = ['reino do cogumelo', 'navio pirata', 'castelo', 'gramado', 'buraco']
combina_listas(personagens, acoes, locais)