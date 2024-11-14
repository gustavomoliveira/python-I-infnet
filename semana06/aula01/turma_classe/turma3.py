""" Classes e Orientação a Objetos """

from models import *

def validar_nome():
    while True:
        nome = input('Digite o nome do aluno: ')
        if len(nome) < 2:
            print('ERRO: Digite um nome válido.')
        else:
            break
    return nome

def validar_nota(txt):
    while True:
        try:
            nota = float(input(txt))
            return nota
        except ValueError:
            print('ERRO: Digite um número válido.')

def entrar_alunos():
    FLAG = 'fim'
    turma = []
    nome = validar_nome()
    while nome.lower() != FLAG:
        nota1 = validar_nota('Digite a primeira nota: ')
        nota2 = validar_nota('Digite a segunda nota: ')
        aluno = Aluno(nome, nota1, nota2)
        turma.append(aluno)
        nome = validar_nome()
    return turma

def exibir_turma(turma):
    for aluno in turma:
        print(aluno) # pega o tostring de models e imprime
    print()

def exibir_medias(turma):
    for aluno in turma:
        print(f'{aluno.nome} {aluno.calcular_media()}')
    print()

def exibir_aprovacao(turma):
    for aluno in turma:
        if aluno.calcular_media() >= 6:
            print(aluno.nome, ' - Aprovado')
        else:
            print(aluno.nome, ' - Prova Final')

turma = entrar_alunos()
exibir_turma(turma)
exibir_medias(turma)
exibir_aprovacao(turma)

