""" 
3 - Escreva um programa que receba dois nomes de usuário e
os combine de maneira criativa para formar um novo nome.
 """

# Valida que o usuário apenas digite letras/caracteres
def valida_texto(texto):
    while True:
        nome = input(texto)
        if all(palavra.isalpha() for palavra in nome.split()):
            return nome
        else:
            print('Erro: Digite apenas letras/caracteres: ')

# Pede os dois nomes ao usuário. O primeiro será invertido e o segundo capitalizado
def pede_input():
    nome_1 = valida_texto('Digite o primeiro nome: ')[::-1]
    nome_2 = valida_texto('Digite o segundo nome: ').title()
    return nome_1, nome_2

nome_1, nome_2 = pede_input()

# Aplica alguns métodos de string para criar algo novo
nome_1 = nome_1.replace(nome_1[-1], 'aeiou')
nome_2 = nome_2.ljust(20, 'A')
novo_nome = nome_1 + nome_2
print(f'Seu novo nome é: {novo_nome}')
