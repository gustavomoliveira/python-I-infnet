""" 
5 - Crie um programa que peça ao usuário seu nome e sobrenome usando input e,
em seguida, combine-os para formar uma saudação personalizada.
 """

def valida_texto(texto):
    while True:
        palavra = input(texto)
        if all(caractere.isalpha() for caractere in palavra.split()):
            return palavra
        else:
            print('Erro: Digite apenas letras/caracteres: ')

def saudacao(nome, sobrenome):
    nome_completo = nome + ' ' + sobrenome
    print(f'Olá, {nome_completo}!')

nome = input('Digite seu nome: ').title()
sobrenome = input('Digite seu sobrenome: ').title()

saudacao(nome, sobrenome)

