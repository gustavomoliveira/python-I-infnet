
def validar_nome(txt):
    while True:
        nome = input(txt)
        if all(letra.isalpha() or letra.isspace() for letra in nome):
            return nome
        else:
            print('ERRO: Digite apenas letras/caracteres.')

def validar_nota(txt):
    while True:
        try:
            nota = float(input(txt))
            if 0 <= nota <= 10:
                return nota
        except ValueError:
            print('ERRO: Digite apenas números.')

def entrar_dados():
    turma = []
    while True:
        nome = validar_nome('Digite o nome do aluno (ou "FIM" para encerrar): ').upper()
        if nome == 'FIM':
            print('Entrada de dados encerrada.')
            print()
            break
        else:
            nota1 = validar_nota('Digite a primeira nota: ')
            nota2 = validar_nota('Digite a segunda nota: ')
            aluno = [nome, nota1, nota2]
            turma.append(aluno)
    return turma

def calcular_media(turma):
    alunos_e_medias = []
    for aluno in turma:
        soma = aluno[1] + aluno[2]
        media = soma / 2
        aluno_e_media = [aluno[0], media]
        alunos_e_medias.append(aluno_e_media)
    return alunos_e_medias

def exibir_aluno_e_media(alunos_e_medias):
    for item in alunos_e_medias:
        print(f'{item[0].title()} possui média {round(item[1], 2)}.')
    print()

def exibir_aprovação(medias):
    for media in medias:
        if media[1] >= 6:
            print(f'{media[0].title()} está APROVADO(A) com média {round(media[1], 2)}')
        else:
            print(f'{media[0].title()} está EM PROVA FINAL com média {round(media[1], 2)}')
    print()

def calcular_media_turma(alunos_e_medias):
    soma_medias = 0
    for aluno in alunos_e_medias:
        soma_medias += aluno[1]

    media_turma = soma_medias / len(alunos_e_medias)
    return media_turma
    
turma = entrar_dados()
alunos_e_medias = calcular_media(turma)
exibir_aluno_e_media(alunos_e_medias)
exibir_aprovação(alunos_e_medias)
media_turma = calcular_media_turma(alunos_e_medias)
print(f'A média geral da turma é {round(media_turma, 2)}')
print()