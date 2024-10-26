"""
Leia uma sequência de nomes de duas notas terminadas por 'fim'
Mostre a media dos alunos
Mostre os alunos aprovados e em prova final (media >= 6) com nome
Faça listas separadas
"""

def entrar_nome():
    nome = input('Digite o nome do aluno: ')
    return nome

def entrar_nota(mensagem):
    nota = int(input(mensagem))
    return nota

def entrar_alunos():
    FIM = 'fim'
    nomes = []
    notas1 = []
    notas2 = []
    nome = entrar_nome()
    while (nome != FIM):
        nomes.append(nome)
        notas1.append(entrar_nota('Digite a primeira nota: '))
        notas2.append(entrar_nota('Digite a segunda nota: '))
        nome = entrar_nome()
    return nomes, notas1, notas2

def calcular_media(notas1, notas2):
    medias = []
    for i in range(len(nomes)):
        media = (notas1[i] + notas2[i]) / 2
        medias.append(media)
    return medias

def exibir_medias(nomes, medias):
    for nome, media in zip(nomes, medias):
        print(nome, media)

def exibir_aprovacao(nomes, medias):
    for nome, media in zip(nomes, medias):
        if media >= 6:
            print(f'{nome} está Aprovado.')
        else:
            print(f'{nome} está na Prova Final.')


nomes, notas1, notas2 = entrar_alunos()
medias = calcular_media(notas1, notas2)
exibir_medias(nomes, medias)
exibir_aprovacao(nomes, medias)