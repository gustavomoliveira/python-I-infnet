""" 
13 - Desenvolva um programa que verifique se uma palavra ou frase
inserida pelo usuário é um palíndromo (lê-se igual de trás para frente).
 """

def valida_texto(texto):
    while True:
        palavra = input(texto)
        if all(caractere.isalpha() for caractere in palavra.split()):
            return palavra
        else:
            print('Erro: Digite apenas letras/caracteres: ')

def confere_palindromo(texto):
    if texto == texto[::-1]:
        return f'A palavra "{texto}" é palíndromo!'
    else:
        return f'A palavra "{texto}" NÃO é palíndromo.'


texto = valida_texto('Digite uma palavra ou frase qualquer: ').lower()
eh_palindromo = confere_palindromo(texto)
print(eh_palindromo)