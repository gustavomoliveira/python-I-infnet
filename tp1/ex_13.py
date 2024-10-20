""" 
13 - Desenvolva um programa que verifique se uma palavra ou frase
inserida pelo usuário é um palíndromo (lê-se igual de trás para frente).
 """

def confere_palindromo(palavra):
    if palavra == palavra[::-1]:
        print(f'A palavra "{palavra}" é palíndromo!')
    else:
        print(f'A palavra "{palavra}" NÃO é palíndromo.')


palavra = str(input('Digite uma palavra qualquer: ').lower())
confere_palindromo(palavra)