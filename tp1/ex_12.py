""" 
12 - Crie um programa que classifique as palavras inseridas
pelo usuário como curtas (menos de 5 letras) ou longas (5 letras ou mais).
 """

def comprimento_palavra(palavra):
    if len(palavra) < 5:
        print(f'A palavra "{palavra}" é curta.')
    else: 
        print(f'A palavra "{palavra}" é longa.')


palavra = str(input('Digite uma palavra qualquer: ')).lower()
comprimento_palavra(palavra)