"""
15 - Cálculo de Médias de Alunos

Faça um programa que leia uma sequência de nomes de alunos de uma turma,
terminada por "FIM", além de suas duas notas (entre 0 e 10).

Para cada aluno, o programa deve informar:
Média do aluno
Se o aluno está aprovado ou em prova final (Média ≥ 6 = Aprovado).
Ao final, o programa deve mostrar a média geral da turma.
Utilize a função de arredondamento para exibir as médias.
Implemente as funções:
Entrada do nome e das notas.
Cálculo da média do aluno.
Cálculo da média da turma.
"""


def calcular_media(lista):
    medias = []
    for aluno in lista:
        soma = aluno[1] + aluno[2]
        media = soma / 2
        medias.append(media)
    return medias

def exibir_aprovação(medias):
    for media in medias:
        print(media)
        if media >= 6:
            print(f'Aprovado com média {round(media, 2)}')
        else:
            print(f'Em Prova Final com média {round(media, 2)}')

def calcular_media_turma(medias):
    media_turma = sum(medias) / len(medias)
    return media_turma

lista_alunos = [['Gustavo', 8, 7], ['Mari', 9, 8], ['Bartô', 3, 4]]
medias = calcular_media(lista_alunos)
print(medias)
exibir_aprovação(medias)
media_turma = calcular_media_turma(medias)
print(round(media_turma, 2))