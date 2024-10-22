""" 
5 - Crie um programa que peça ao usuário seu nome e sobrenome usando input e,
em seguida, combine-os para formar uma saudação personalizada.
 """

def saudacao(nome, sobrenome):
    nome_completo = nome + ' ' + sobrenome
    print(f'Olá, {nome_completo}!')

nome = input('Digite seu nome: ').title()
sobrenome = input('Digite seu sobrenome: ').title()
saudacao(nome, sobrenome)


