""" 
3 - Escreva um programa que receba dois nomes de usuário e
os combine de maneira criativa para formar um novo nome.
 """

nome_1 = input('Digite o primeiro nome: ')[::-1]
nome_2 = input('Digite o segundo nome: ').title()


nome_1 = nome_1.replace(nome_1[-1], 'aeiou')
nome_2 = nome_2.ljust(20, 'A')
novo_nome = nome_1 + nome_2
print(f'Seu novo nome é: {novo_nome}')
