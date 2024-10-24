""" 
12 - Crie um programa que classifique as palavras inseridas
pelo usuário como curtas (menos de 5 letras) ou longas (5 letras ou mais).
 """

def valida_texto(texto):
    while True:
        palavra = input(texto)
        if all(caractere.isalpha() for caractere in palavra.split()):
            return palavra
        else:
            print('Erro: Digite apenas letras/caracteres: ')

def comprimento_palavra(palavra):
    if len(palavra) < 5:
        print(f'A palavra "{palavra}" é curta.')
    else: 
        print(f'A palavra "{palavra}" é longa.')


palavra = valida_texto('Digite uma palavra qualquer: ').lower()
comprimento_palavra(palavra)