""" Listas de listas """

def validar_nome(): # regra de negócio para validar n˚ de caracteres em nome
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
    nome = validar_nome() # se for digitado 'fim' o aluno nem entra no while
    while nome.lower() != FLAG:
        nota1 = validar_nota('Digite a primeira nota: ')
        nota2 = validar_nota('Digite a segunda nota: ')
        aluno = [nome, nota1, nota2]
        turma.append(aluno)
        nome = validar_nome()
    return turma

def exibir_turma(turma):
    for aluno in turma:
        print(f'{aluno[0]}, {aluno[1]}, {aluno[2]}') # formatação para eliminar os colchetes
    print()

def calcular_media(turma):
    medias = []
    for aluno in turma:
        soma = aluno[1] + aluno[2]
        media = soma / 2
        aluno_media = [aluno[0], media]
        medias.append(aluno_media)
    return medias

def exibir_medias(medias):
    for media in medias:
        print(media)
    print()

def exibir_aprovacao(medias):
    for media in medias:
        if media[1] >= 6: # foi necessário a indexação de 1 por causa da forma que media foi criada, contendo também o nome do aluno no index 0
            print(media[0], ' - Aprovado')
        else:
            print(media[0], ' - Prova Final')

turma = entrar_alunos()
exibir_turma(turma)
medias = calcular_media(turma)
exibir_medias(medias)
exibir_aprovacao(medias)

# forma tradicional
""" for i in range(len(turma)):
    print(turma[i])
print() """

# forma limpa (pythonic) --> equivalente a forEach do JS
""" for aluno in turma:
    print(aluno) """

# usar SEMPRE passagem de parâmetro para as funções. evitar declarações globais.
